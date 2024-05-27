# Телеграм-бот для генерации QR-кодов

Этот репозиторий содержит исходный код телеграм-бота, который генерирует QR-коды. Бот позволяет пользователям легко создавать QR-коды, отправляя текстовые сообщения. Кроме того, пользователи могут настраивать цвет своих QR-кодов через интерфейс бота.

## Функциональные возможности

- **Создание QR-кодов:** Просто отправьте текстовое сообщение боту, и он сгенерирует для вас QR-код.
- **Настройка цвета QR-кода:** Выберите из множества цветов для настройки вашего QR-кода.
- **Удобство использования:** Интуитивно понятные команды и интерфейс для бесшовного пользовательского опыта.

## Требования

Для запуска бота требуются следующие пакеты Python:

- aiofiles==23.2.1
- aiogram==3.6.0
- aiohttp==3.9.5
- aiosignal==1.3.1
- annotated-types==0.7.0
- attrs==23.2.0
- certifi==2024.2.2
- colorama==0.4.6
- frozenlist==1.4.1
- idna==3.7
- install==1.3.5
- magic-filter==1.0.12
- multidict==6.0.5
- pydantic==2.7.1
- pydantic_core==2.18.2
- pypng==0.20220715.0
- python-dotenv==1.0.1
- segno==1.6.1
- typing_extensions==4.12.0
- yarl==1.9.4

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/yourusername/qr-code-generator-bot.git
    cd qr-code-generator-bot
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

3. Создайте файл `.env` с вашим токеном бота:
    ```
    TOKEN=your_telegram_bot_token
    ```

## Использование

1. Запустите бота:
    ```bash
    python main.py
    ```

2. Начните диалог с вашим ботом в Телеграме.

3. Отправьте текстовое сообщение для создания QR-кода.

4. Используйте встроенную клавиатуру для настройки цвета вашего QR-кода.

## Команды бота

- **/start:** Инициализирует бота и предоставляет инструкции.
- **Текстовое сообщение:** Отправьте текстовое сообщение для создания QR-кода.
- **Встроенная клавиатура:** Выберите цвет для настройки вашего QR-кода.

## Основной код

Основная функциональность бота реализована в `main.py`, который инициализирует бота и настраивает обработчики команд. Логика генерации QR-кодов находится в функции `create_code` в файле `utils/qr.py`. Бот использует библиотеку Aiogram для взаимодействия с API Телеграм и Segno для генерации QR-кодов.

### Пример кода

```python
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import Config
from handlers.base import user_router

async def main():
    logging.basicConfig(level=logging.INFO)
    config = Config()
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
    bot = Bot(token=config.token, default=default)
    dp = Dispatcher()
    dp.include_routers(user_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    run(main())
```

## Вклад

Вклады приветствуются! Пожалуйста, не стесняйтесь отправлять запрос на слияние или открывать issue для обсуждения улучшений или новых функций.

## Лицензия

Этот проект лицензирован на условиях лицензии MIT. См. файл LICENSE для подробностей.

---

Наслаждайтесь генерацией QR-кодов с помощью вашего нового телеграм-бота! Если у вас есть вопросы или вам нужна дополнительная помощь, не стесняйтесь обращаться.
