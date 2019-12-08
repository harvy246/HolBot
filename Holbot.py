import telegram

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


Holbot_token = '920440470:AAFyx6W52X05KlvaXC-XEVm4OpiEpSJBGeE'
Holbot = telegram.Bot(token = Holbot_token)
updates = Holbot .getUpdates()
for u in updates:
    print(u.message)


import sys
import HolBotModel

def proc_hello(bot, update):
    Holbot.sendMessage('원하시는 광고 방법을 선택하세요.')



def proc_stop(bot, update):
    Holbot.sendMessage('서비스가 종료됩니다.')
    Holbot.stop()

def build_box(buttons,n_cols, header_buttons = None, footer_buttons = None):
    menu = [buttons[i:i + n_cols] for i in range (0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu



def proc_test(bot, update):
    t = "안녕하세요 홀봇입니다.";
    Holbot.sendMessage(self_id = update.message.self_id,text = t)
    show_list = []
    show_list.append(InlineKeyboardButton("자동 광고",callback_data = "자동 광고"))
    show_list.append(InlineKeyboardButton("지금 광고",callback_data = "지금 광고"))
    show_markup = InlineKeyboardMarkup(build_box(show_list, len(show_list)-1))
    update.message.reply_text("원하시는 광고 방법을 선택하세요.", reply_markup = show_markup)


Holbot = HolBotModel.Bot5885()
Holbot.add_handler('hello', proc_hello)
Holbot.add_handler('test',proc_test)
Holbot.add_handler('stop', proc_stop)
Holbot.start()

