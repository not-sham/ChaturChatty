import telepot
from KEYS import TELEGRAM_KEY


class TelegramBot(object):
	def __init__(self):
		self.bot = telepot.Bot(TELEGRAM_KEY)

	def keep_ears_open(self):
		"""
		keeps listening to the incoming texts
		:return:
		"""
		print(self.bot.getUpdates())

	def do_init(self):
		pass

	def send_message(self, chat_id, text):
		self.bot.sendMessage(chat_id=chat_id, text=text)

	def parse_message(self):
		# self.
		pass

	def run(self):
		self.do_init()


if __name__ == "__main__":
	t = TelegramBot()
	t.keep_ears_open()

# for u in bot.get_updates():
# 	print(u.message.text)
# 	# main.WeatherMan(u.message.text).run()
# 	bot.send_message(chat_id=u.message.chat.id, text="Shyam is still working on how to make me smart.. Give him sometime")
#
#
# 	# try to cache the response of the std user query. Need to know what he means not what he typed
#
# 	# try to seperate out the latest response of the user