# Text-to-speach
A simple Telegram bot built with Python that translates Persian text into English, Spanish, or French and converts it into natural speech using Google Text-to-Speech (gTTS).
# 🎙️ Telegram Text to Voice Bot

A simple Telegram bot built with **Python** that translates Persian text into multiple languages and converts it into natural speech using **Google Text-to-Speech (gTTS)**.

## ✨ Features

- 🌍 Translate Persian text
- 🔊 Convert translated text to voice
- 🇬🇧 English support
- 🇪🇸 Spanish support
- 🇫🇷 French support
- 🎯 Language selection using inline buttons
- 📁 Temporary audio file creation
- 🗑️ Automatic file deletion after sending
- ⚡ Fast and lightweight

---

## 📦 Technologies

- Python
- pyTelegramBotAPI
- gTTS
- googletrans
- python-dotenv

---

## 📁 Project Structure

```
text-to-voice-bot/
│
├── voices/
├── .env
├── bot.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/text-to-voice-bot.git

cd text-to-voice-bot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create `.env`

```env
API_TOKEN=YOUR_BOT_TOKEN
```

### Run

```bash
python bot.py
```

---

## 📚 Requirements

```
pyTelegramBotAPI
gTTS
googletrans
python-dotenv
```

or

```bash
pip install pyTelegramBotAPI gTTS googletrans python-dotenv
```

---

## 🚀 How It Works

1. Start the bot with `/start`
2. Choose a language
3. Send a Persian text
4. The bot translates the text
5. Converts it into speech
6. Sends the generated voice message

---

## 💬 Example

User:

```
سلام، حالت چطوره؟
```

Selected language:

```
English
```

Bot generates:

```
Hello, how are you?
```

and sends it as a voice message.

---

## 📸 Supported Languages

| Language | Code |
|----------|------|
| English | en |
| Spanish | es |
| French | fr |

---

## 🔒 Environment Variables

| Variable | Description |
|----------|-------------|
| API_TOKEN | Telegram Bot Token |

---

## 📌 Future Improvements

- More languages
- Text language auto detection
- Adjustable speech speed
- Voice settings
- Save conversion history
- Better error handling
- Docker support
- Deploy on VPS

---

## 👨‍💻 Author

**Arash Tqv**

Python Developer | Telegram Bot Developer

---

## ⭐ If you like this project, don't forget to star the repository!
