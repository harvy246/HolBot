import telegram
from telegram.ext import Updater, CommandHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 707415970
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()


class Bot5885(TelegramBot):
    def __init__(self):
        self.token = '920440470:AAFyx6W52X05KlvaXC-XEVm4OpiEpSJBGeE'
        TelegramBot.__init__(self, '홀봇', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('홍보를 원하시는 사진을 보내주세요.')
        self.updater.start_polling()
        self.updater.idle()


