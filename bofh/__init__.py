import importlib.resources
import random
from typing import Literal

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


class BofhBot(Plugin):
    async def _read_excuse_file(self, filename: str) -> str:
        path = f"bofh/{filename}"
        data: bytes
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

    @command.new(name="excuse", help="Get a random BOFH excuse.")
    async def excuse_handler(self, evt: MessageEvent) -> None:
        await self._send_excuse(evt, "excuses.txt", "en")

    @command.new(
        name="отмазка",
        help="Случайная системная отмазка.",
        aliases=("otmazka",),
    )
    async def otmazka_handler(self, evt: MessageEvent) -> None:
        await self._send_excuse(evt, "excuses_ru.txt", "ru")
