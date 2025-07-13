# 🤖 Personal AI Telegram Bot

A private Telegram bot that generates AI-powered responses using OpenRouter.  
Built with `aiogram` and designed for restricted access — only selected user IDs can use the bot.

---

## 🚀 Features

- Asynchronous message generation via OpenRouter
- Built with `aiogram` 3.x (Telegram bot framework)
- Environment-based configuration with `.env`
- Restricted to specific Telegram user IDs (anti-flood)

---

## ⚙️ Installation

```bash
git clone https://github.com/reqv1em/personal-AI-telegram-bot.git
cd personal-AI-telegram-bot
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🧪 .env Configuration

Create a `.env` file in the root directory and add the following:

```env
TELEGRAM_TOKEN=your_telegram_bot_token
BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=deepseek/deepseek-r1
RID=123456789  # your Telegram user ID
LID=987654321  # second allowed user ID (optional)
```

---

## 📦 Run the bot

```bash
python run.py
```

---

## 🔐 Access Restriction

Only the two Telegram user IDs defined in `RID` and `LID` can interact with the bot.  
Any other user will be silently ignored.

---

## 🛠️ Technologies Used

- Python 3.11+
- [aiogram](https://docs.aiogram.dev/en/latest/)
- [OpenRouter](https://openrouter.ai/)
- [dotenv](https://pypi.org/project/python-dotenv/)