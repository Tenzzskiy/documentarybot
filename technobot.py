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
    bot.send_message(message.chat.id,"Добро пожаловать! {} 👋 \nЯ Юрист Ассистент, а ниже представлены команды, которые я могу выполнять 🤖",reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "faq":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        alim_button = types.InlineKeyboardButton(text="Соглашение об алиментах", callback_data="alim")
        back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
        keyboard.add(alim_button, back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="❓ Ниже представлен список документо, выберите подходящий раздел по вашей проблеме", reply_markup=keyboard)
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
    elif call.data =="alim":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton(text="Вернуться назад", callback_data="back")
        keyboard.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Для составления документа напишите команду '/doc '",
                              reply_markup=keyboard)
    elif call.data == "about":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        func_button = types.InlineKeyboardButton(text="Что я могу?",callback_data="func")
        boss_button = types.InlineKeyboardButton(text="Информация о правообладателе",callback_data="boss")
        back_button = types.InlineKeyboardButton(text = "Назад",callback_data="back")
        keyboard.add(func_button,boss_button,back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Что я могу?"
        ,reply_markup=keyboard)


    elif call.data == "pravodoc":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        consult_button = types.InlineKeyboardButton(text="Консультации",callback_data="consult")
        dogovor_button = types.InlineKeyboardButton(text="Все о договорах",callback_data="dogovor")
        gr_button = types.InlineKeyboardButton(text="Гражданское прааво",callback_data="gr")
        adm_button = types.InlineKeyboardButton(text="Административное право",callback_data="amd")
        home_button = types.InlineKeyboardButton(text="Жилищное право",callback_data="home")
        spor_button = types.InlineKeyboardButton(text="Оспаривание судебных решений",callback_data="spor")
        back_button = types.InlineKeyboardButton(text = "Назад",callback_data="back")
        keyboard.add(consult_button,dogovor_button,gr_button,adm_button,home_button,spor_button,back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Разборы правовых ситуаций"
        ,reply_markup=keyboard)


    elif call.data=="consultation":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        feedback_button = types.InlineKeyboardButton(text="Обратный звонок", callback_data="feedback")
        cont_button = types.InlineKeyboardButton(text="Контакты Юриста",callback_data="cont")
        back_button = types.InlineKeyboardButton(text = "Назад",callback_data="back")
        keyboard.add(cont_button,feedback_button,back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Как с нами связаться"
        ,reply_markup=keyboard)
    elif call.data=="business":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        sponsor_button = types.InlineKeyboardButton(text="Стать партнером",callback_data="sponsor")
        reklama_button = types.InlineKeyboardButton(text="Реклама",callback_data="reklama")
        back_button = types.InlineKeyboardButton(text = "Назад",callback_data="back")
        keyboard.add(reklama_button,sponsor_button,back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Партнерство"
        ,reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/doc':
        global graph1
        bot.send_message(message.from_user.id, "Введите ваше ФИО в формате: Александров Александр Александрович")
        bot.register_next_step_handler(message, get_1)
    else:
        bot.send_message(message.from_user.id, 'Соглашение об алиментах "/doc"')
def get_1(message):
    global FIO1
    bot.send_message(message.from_user.id, 'Введите номер и серию паспорта в формате : 4615 123456')
    bot.register_next_step_handler(message, get_2)
    FIO1 = message.text
def get_2(message):
    global pass1
    bot.send_message(message.from_user.id, 'Введите адрес проживания')
    bot.register_next_step_handler(message, get_3)
    pass1 = message.text
def get_3(message):
    global adress1
    bot.send_message(message.from_user.id, 'Введите ФИО плательщика в формате: Александров Александр Александрович')
    bot.register_next_step_handler(message, get_4)
    adress1 = message.text
def get_4(message):
    global FIO2
    bot.send_message(message.from_user.id, 'Введите номер и серию паспорта плательщика в формате : 4615 123456')
    bot.register_next_step_handler(message, get_5)
    FIO2 = message.text
def get_5(message):
    global pass2
    bot.send_message(message.from_user.id, 'Введите адрес проживания плательщика')
    bot.register_next_step_handler(message, get_6)
    pass2 = message.text
def get_6(message):
    global adress2
    bot.send_message(message.from_user.id, 'Чтобы завершить заполнение напишите "Готово"')
    bot.register_next_step_handler(message, get_final)
    adress2 = message.text
def get_final(message):
    bot.send_message(message.from_user.id, 'Ваш готовый файл')
    doc = DocxTemplate("/Users/aleksandrten/Downloads/github/technobot/shablon.docx")
    context = { 'FIO1' : FIO1, 'pass1' : pass1, 'adress1' : adress1, 'FIO2' : FIO2, 'pass2' : pass2, 'adress2' : adress2 }
    doc.render(context)
    doc.save("/Users/aleksandrten/Downloads/github/technobot/finalcut.docx")
    doc = open("/Users/aleksandrten/Downloads/github/technobot/finalcut.docx", "rb")
    bot.send_document(message.chat.id, doc)


if __name__ == '__main__':
    bot.infinity_polling()
