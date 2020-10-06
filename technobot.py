from telegram import Bot;
from telegram import Update;
from telegram.ext import Updater;
from telegram.ext import CommandHandler;
from telegram.ext import MessageHandler;
from telegram.ext import Filters;
import telebot
from telebot import types #maxim bog
from docxtpl import DocxTemplate

TG_TOKEN = "957294714:AAFJRRACBuGuzUNFPZYMDQhn_mDZBffJwUU"

bot = telebot.TeleBot("957294714:AAFJRRACBuGuzUNFPZYMDQhn_mDZBffJwUU")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    pravodoc_button = types.InlineKeyboardButton(text="Разборы правовых ситуаций с документами", callback_data='pravodoc')
    faq_button = types.InlineKeyboardButton(text="Ответы на часто встречаемые ситуации", callback_data="faq")
    konsultation_button = types.InlineKeyboardButton(text="Запись на консультацию", callback_data='konsultation')
    business_button = types.InlineKeyboardButton(text="Для бизнеса", callback_data='business')
    about_button = types.InlineKeyboardButton(text="О боте", callback_data='about')
    keyboard.add(faq_button, konsultation_button, pravodoc_button, business_button, about_button)
    bot.send_message(message.chat.id,"Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖",
                     reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def handle_start_text(message):
    if message.text == "Максон":
        bot.send_message(message.chat.id, "Да\nДа Да\nЭт я)")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    pravodoc_button = types.InlineKeyboardButton(text="Разборы правовых ситуаций с документами", callback_data="pravodoc")
    faq_button = types.InlineKeyboardButton(text="Ответы на часто встречаемые ситуации", callback_data="faq")
    konsultation_button = types.InlineKeyboardButton(text="Запись на консультацию", callback_data='konsultation')
    business_button = types.InlineKeyboardButton(text="Для бизнеса", callback_data='business')
    about_button = types.InlineKeyboardButton(text="О боте", callback_data='about')
    keyboard.add(faq_button, konsultation_button, pravodoc_button, business_button, about_button)
    bot.send_message(message.chat.id,
                     "Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "faq":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        qa1_button = types.InlineKeyboardButton(text="Распитие в общественном месте", callback_data="qa1")
        back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
        keyboard.add(qa1_button, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="❓ Ниже представлен список часто задаваемых вопросов ❓", reply_markup=keyboard)
        # Уведомление в верхней части экрана
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Cписок задаваемых вопросов!")
    elif call.data == "back":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        pravodoc_button = types.InlineKeyboardButton(text="Разборы правовых ситуаций с документами", callback_data="pravodoc")
        faq_button = types.InlineKeyboardButton(text="Ответы на часто встречаемые ситуации", callback_data="faq")
        konsultation_button = types.InlineKeyboardButton(text="Запись на консультацию", callback_data='konsultation')
        business_button = types.InlineKeyboardButton(text="Для бизнеса", callback_data='business')
        about_button = types.InlineKeyboardButton(text="О боте", callback_data='about')
        keyboard.add(faq_button, konsultation_button, pravodoc_button, business_button, about_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Добро пожаловать!👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖",
                              reply_markup=keyboard)

    elif call.data == "pravodoc":
        doc_full()
        
@bot.message_handler(content_types=["text"])
def doc_full(message):
    doc = DocxTemplate("/Users/aleksandrten/Downloads/github/technobot/shablon.docx")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    bot.send_message(message.chat.id,"Введите название компании", reply_markup=keyboard)
    graph1 = message.text
    #bot.wait
    bot.send_message(message.chat.id,"Введите адрес компании", reply_markup=keyboard)
    graph2 = message.text
    #bot.wait
    context = { 'emitent' : graph1, 'address1' : graph2, 'участник': 'ООО Участник', 'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 'director': 'И.И. Иванов'}
    doc.render(context)
    doc.save("/Users/aleksandrten/Downloads/github/technobot/finalcut.docx")




if __name__ == '__main__':
    bot.infinity_polling()
