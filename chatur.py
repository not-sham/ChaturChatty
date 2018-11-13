import enchant


from nltk.tokenize import sent_tokenize as st
from nltk import word_tokenize as wt
from nltk.metrics import edit_distance
from wit import Wit

from KEYS import WIT_API_KEY


class DoNLPThingy(object):
	def __init__(self, sentence):
		self.spell_dict = enchant.Dict("en_US")
		self.wit = Wit(WIT_API_KEY)
		self.dialogs = st(sentence)
		self.resp = None
		self.entities = None
		self.WEATHER_ENTITIES = ["CLOUD", "RAIN", "TEMPERATURE", "HUMIDITY", "SUNSET", "SUNRISE", "TIME",
								"SNOW", "PRESSURE", "HEAT", "DETAILS", "WIND", "VISIBILITY", "WEATHER"]
		self.context_dict = dict()

	def auto_correct(self, word):
		if self.spell_dict.check(word):
			return word
		suggestions = self.spell_dict.suggest(word)
		if suggestions and edit_distance(word, suggestions[0]) <= 1:
			return suggestions[0]
		else:
			return word

	def pre_processing(self):
		print("Trying to auto-correct the user input '%s'" % (self.dialog,))
		self.dialog = (" ".join([self.auto_correct(word) for word in wt(self.dialog)]))
		print("to '%s'" % self.dialog)

	def better_call_wit(self):
		self.resp = self.wit.message(self.dialogs)

	def post_processing(self):
		self.entities = self.resp['entities']
		self.get_intent()

	def get_intent(self):
		for k in self.entities.keys():
			for loc in [loc['value'] for loc in self.entities.get('location')]:
				if k in [w.lower() for w in self.WEATHER_ENTITIES]:
					if loc not in self.context_dict.values():
						self.context_dict[k] = loc

	def run(self):
		for each_dialog in self.dialogs:
			# try multi process here...
			self.dialog = each_dialog
			self.pre_processing()
			self.better_call_wit()
			self.post_processing()
			print(self.context_dict)
			return self.context_dict


if __name__ == "__main__":
	d = DoNLPThingy("weather in bangalore")
	d.run()
