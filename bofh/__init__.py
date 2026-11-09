import importlib.resources
import random
from typing import Literal, Type

from mautrix.util.config import BaseProxyConfig, ConfigUpdateHelper

from maubot import Plugin, MessageEvent
from maubot.handlers import command

Locale = Literal["en", "ru"]

_MESSAGES: dict[Locale, dict[str, str]] = {
    "en": {
        "empty": "The excuse file is empty. The problem exists between the keyboard and chair.",
        "not_found": "Error: excuses file not found inside the plugin package. The build is broken.",
        "read_error": "A critical error occurred reading the excuses file.",
    },
    "ru": {
        "empty": "Файл отмазок пуст. Проблема между клавиатурой и стулом.",
        "not_found": "Ошибка: файл отмазок не найден в пакете плагина. Сборка сломана.",
        "read_error": "Критическая ошибка при чтении файла отмазок.",
    },
}


class Config(BaseProxyConfig):
    def do_update(self, helper: ConfigUpdateHelper) -> None:
        helper.copy("command_en")
        helper.copy("command_ru")
        helper.copy("command_ru_aliases")


class BofhBot(Plugin):
    async def start(self) -> None:
        self.config.load_and_update()

    def on_external_config_update(self) -> None:
        self.config.load_and_update()

    @classmethod
    def get_config_class(cls) -> Type[BaseProxyConfig]:
        return Config

    def en_command_name(self) -> str:
        return self.config["command_en"]

    def ru_command_match(self, val: str) -> bool:
        primary = str(self.config["command_ru"]).lower()
        if val == primary:
            return True
        aliases = self.config["command_ru_aliases"] or []
        return val in {str(alias).lower() for alias in aliases}

    async def _read_excuse_file(self, filename: str) -> str:
        path = f"bofh/{filename}"
        try:
            data = await self.loader.read_file(path)
        except AttributeError:
            data = (
                importlib.resources.files("bofh")
                .joinpath(filename)
                .read_bytes()
            )
        return data.decode("utf-8")

    async def get_random_excuse(self, filename: str, locale: Locale) -> str:
        messages = _MESSAGES[locale]
        try:
            excuses_text = await self._read_excuse_file(filename)
            excuses = [
                line.strip() for line in excuses_text.strip().split("\n") if line.strip()
            ]

            if not excuses:
                return messages["empty"]

            return random.choice(excuses)
        except (FileNotFoundError, KeyError):
            self.log.error("%s not found inside the plugin package!", filename)
            return messages["not_found"]
        except Exception:
            self.log.exception("Failed to read excuse file %s", filename)
            return messages["read_error"]

    async def _send_excuse(
        self, evt: MessageEvent, filename: str, locale: Locale
    ) -> None:
        await self.client.set_typing(evt.room_id, True)
        try:
            excuse = await self.get_random_excuse(filename, locale)
            await self.client.send_text(evt.room_id, excuse)
        finally:
            await self.client.set_typing(evt.room_id, False)

    @command.new(
        name=lambda self: self.en_command_name(),
        help="Get a random BOFH excuse.",
    )
    async def excuse_handler(self, evt: MessageEvent) -> None:
        await self._send_excuse(evt, "excuses.txt", "en")

    @command.new(
        name=lambda self: str(self.config["command_ru"]),
        help="Случайная системная отмазка.",
        aliases=ru_command_match,
    )
    async def otmazka_handler(self, evt: MessageEvent) -> None:
        await self._send_excuse(evt, "excuses_ru.txt", "ru")
