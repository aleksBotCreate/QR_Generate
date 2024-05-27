# QR Code Generator Telegram Bot

This repository contains the source code for a Telegram bot that generates QR codes. The bot allows users to easily create QR codes by sending text messages. Additionally, users can customize the color of their QR codes through the bot's interface.

## Features

- **Generate QR Codes:** Simply send a text message to the bot, and it will generate a QR code for you.
- **Customize QR Code Color:** Choose from a variety of colors to customize your QR code.
- **Easy to Use:** Intuitive commands and interface for a seamless user experience.

## Requirements

The following Python packages are required to run the bot:

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

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/qr-code-generator-bot.git
    cd qr-code-generator-bot
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file with your bot token:
    ```
    TOKEN=your_telegram_bot_token
    ```

## Usage

1. Run the bot:
    ```bash
    python main.py
    ```

2. Start a conversation with your bot on Telegram.

3. Send a text message to generate a QR code.

4. Use the provided inline keyboard to customize the color of your QR code.

## Bot Commands

- **/start:** Initiates the bot and provides instructions.
- **Text Message:** Sends a text message to generate a QR code.
- **Inline Keyboard:** Select a color to customize your QR code.

## Main Code Overview

The main functionality of the bot is implemented in `main.py`, which initializes the bot and sets up the command handlers. The QR code generation logic is handled by the `create_code` function in the `utils/qr.py` file. The bot uses the Aiogram library for interaction with the Telegram API and Segno for QR code generation.

### Example Code Snippet

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

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss improvements or new features.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy generating QR codes with your new Telegram bot! If you have any questions or need further assistance, feel free to reach out.
