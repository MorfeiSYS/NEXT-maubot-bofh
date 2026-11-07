# Плагин maubot «BOFH Excuse»

Простой плагин для maubot: по команде выдаёт случайную технически правдоподобную отмазку. Подходит, когда нужно съехать с ответственности с помощью жаргона.

Язык ответа зависит от команды:

| Команда | Язык |
|---------|------|
| `!excuse` | английский (классический список отмазок BOFH) |
| `!отмазка` или `!otmazka` | русский (перевод того же списка) |

## Использование

В любой комнате, куда добавлен бот:

```
!excuse
```

```
!отмазка
```

Бот отправит новое сообщение в чат, например:

> Робот-сменщик лент принял галстук оператора за ленту.

<img width="568" height="204" alt="пример работы бота" src="https://github.com/user-attachments/assets/dc28142e-b712-46ed-9a4d-9ee59179c773" />

## Сборка плагина

Нужны Python и пакет `maubot` (в нём есть утилита `mbc`).

```bash
pip install -r requirements-dev.txt
```

**Windows (PowerShell):**

```powershell
.\build.ps1
```

**Linux / macOS:**

```bash
chmod +x build.sh
./build.sh
```

**Вручную** (из каталога с `maubot.yaml`):

```bash
mbc build
```

На выходе — файл `.mbp` в корне проекта (игнорируется git).

Для разработки можно собрать и сразу залить на сервер:

```bash
mbc build -u
```

## Установка

1. Соберите плагин, как описано выше.
2. Загрузите получившийся `.mbp` в веб-интерфейсе вашего экземпляра maubot.
3. Создайте экземпляр плагина и привяжите его к клиенту (учётной записи бота).
4. Пригласите бота в комнаты, где нужны отмазки.

## Отказ от ответственности

Плагин поставляется «как есть». Отмазки взяты из списка в духе юмора 1990-х. Часть формулировок по современным меркам может показаться некорректной; автор плагина не отвечает за содержание самих отмазок.

## Источник и лицензия

Список отмазок основан на классическом **BOFH Excuse File**.

- **Оригинал:** [https://pages.cs.wisc.edu/~ballard/bofh/excuses](https://pages.cs.wisc.edu/~ballard/bofh/excuses)

Автор оригинального списка передал его в общественное достояние (см. [источник](https://metadata.ftp-master.debian.org/changelogs//main/f/fortunes-bofh-excuses/fortunes-bofh-excuses_1.2-3_copyright)).

Русские тексты в `bofh/excuses_ru.txt` — перевод тех же строк в том же порядке, что и в `bofh/excuses.txt`.

Плагин распространяется под LGPL-3. Можно изменять и распространять дальше.

---

# BOFH Excuse Maubot Plugin

A simple maubot plugin that provides a random, technically-plausible excuse upon request. Perfect for any situation where you need to deflect blame with jargon.

The bot responds in the language of the command you use:

| Command | Language |
|---------|----------|
| `!excuse` | English (from the classic BOFH excuse list) |
| `!отмазка` or `!otmazka` | Russian translation of the same list |

## Usage

In any room where the bot is present:

```
!excuse
```

```
!отмазка
```

The bot posts a new message in the chat, for example:

> Robotic tape changer mistook operator's tie for a backup tape.

<img width="568" height="204" alt="bot example screenshot" src="https://github.com/user-attachments/assets/dc28142e-b712-46ed-9a4d-9ee59179c773" />

## Building the plugin

You need Python and the `maubot` package, which includes the `mbc` CLI.

```bash
pip install -r requirements-dev.txt
```

**Windows (PowerShell):**

```powershell
.\build.ps1
```

**Linux / macOS:**

```bash
chmod +x build.sh
./build.sh
```

**Manual build** (from the directory that contains `maubot.yaml`):

```bash
mbc build
```

The output is a `.mbp` file in the project root (ignored by git).

To build and upload in one step during development:

```bash
mbc build -u
```

## Installation

1. Build the plugin as above.
2. Upload the generated `.mbp` file to your maubot instance via the web UI.
3. Create an instance of the plugin, assigning it to a client (bot user).
4. Invite the bot user to any rooms where you want to use it.

## Disclaimer

This plugin is provided "as is". The excuses are sourced from a file reflecting the humor of the 1990s. Some content may be considered politically incorrect by modern standards, and the author of this plugin is not responsible for the content of the excuses.

## Source & License

The list of excuses used by this bot is sourced from the classic **BOFH Excuse File**.

- **Original Source:** [https://pages.cs.wisc.edu/~ballard/bofh/excuses](https://pages.cs.wisc.edu/~ballard/bofh/excuses)

The author of the original list has placed this into the public domain. (as per this [source](https://metadata.ftp-master.debian.org/changelogs//main/f/fortunes-bofh-excuses/fortunes-bofh-excuses_1.2-3_copyright))

Russian texts in `bofh/excuses_ru.txt` are translations of the same lines, kept in the same order as `bofh/excuses.txt`.

This maubot plugin is provided under the LGPL-3. Feel free to modify and redistribute it.
