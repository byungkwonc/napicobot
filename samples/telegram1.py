from accounts import accounts
from telegram.ext import Updater

APT_INFO_TEST_BOT_TOKEN = '1749792111:AAHhGbNY1zcwg76ZwIMgdkYbrae3Gfqi6xI'
CHAT_ID=accounts.TELEGRAM_MY_CHAT_ID

updater = Updater(APT_INFO_TEST_BOT_TOKEN)
updater.bot.send_message(chat_id=CHAT_ID, text='Hello telegram bot!')