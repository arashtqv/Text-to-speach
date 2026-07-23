import telebot
import os
import logging
from dotenv import load_dotenv
from gtts import gTTS
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from googletrans import Translator

load_dotenv()

translator = Translator()

telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

os.makedirs("voices", exist_ok=True)

# زبان انتخابی هر کاربر
user_languages = {}

# ===================== START =====================

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()

    enbtn = InlineKeyboardButton("🇬🇧 English", callback_data="en")
    spbtn = InlineKeyboardButton("🇪🇸 Spanish", callback_data="es")
    frbtn = InlineKeyboardButton("🇫🇷 French", callback_data="fr")

    markup.row(enbtn, spbtn, frbtn)

    bot.send_message(
        message.chat.id,
        "لطفا زبان مورد نظر خود رو انتخاب کنید:",
        reply_markup=markup
    )


# ===================== BUTTON =====================

@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "en":
        user_languages[call.from_user.id] = "en"
        bot.answer_callback_query(call.id, "انگلیسی انتخاب شد")
        bot.send_message(
            call.message.chat.id,
            "حالا متن خود را بفرستید."
        )

    elif call.data == "es":
        user_languages[call.from_user.id] = "es"
        bot.answer_callback_query(call.id, "اسپانیایی انتخاب شد")
        bot.send_message(
            call.message.chat.id,
            "حالا متن خود را بفرستید."
        )

    elif call.data == "fr":
        user_languages[call.from_user.id] = "fr"
        bot.answer_callback_query(call.id, "فرانسوی انتخاب شد")
        bot.send_message(
            call.message.chat.id,
            "حالا متن خود را بفرستید."
        )



# ===================== TEXT =====================

@bot.message_handler(func=lambda message: True)
def text_to_speech(message):

    try:
        bot.send_chat_action(
            message.chat.id,
            "upload_voice"
        )

        text = message.text

        # گرفتن زبان انتخاب شده کاربر
        lang = user_languages.get(message.from_user.id)

        if lang is None:
            bot.reply_to(
                message,
                "اول /start را بزنید و زبان را انتخاب کنید."
            )
            return


        # ترجمه فارسی به زبان انتخاب شده
        result = translator.translate(
            text,
            src="fa",
            dest=lang
        )

        translated_text = result.text


        # ساخت فایل صوتی
        file_name = os.path.join(
            "voices",
            f"{message.id}.mp3"
        )

        voice = gTTS(
            text=translated_text,
            lang=lang,
            tld="com"
        )

        voice.save(file_name)


        # ارسال ویس
        with open(file_name, "rb") as audio:
            bot.send_voice(
                chat_id=message.chat.id,
                voice=audio,
                reply_to_message_id=message.id
            )


        # حذف فایل
        os.remove(file_name)


    except Exception as e:
        bot.reply_to(
            message,
            f"Error: {e}"
        )


bot.infinity_polling()
