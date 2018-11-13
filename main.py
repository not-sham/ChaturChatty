import multiprocessing as mp
from chatur import DoNLPThingy
from weatherApp import WeatherMan


class HouseKeeping(object):
	def __init__(self):
		self.get_cores()
		self.clean_pyc()

	def get_cores(self):
		try:
			PROCESS_LIMIT = mp.cpu_count()
		except ImportError:
			PROCESS_LIMIT = 2

	def clean_pyc(self):
		# to be implemented later
		pass


class EntityExtractor(object):
	def __init__(self, entity):
		self.entity = entity
		self.data = dict()
		self.entities = ["CLOUD", "RAIN", "TEMPERATURE", "HUMIDITY", "SUNSET", "SUNRISE", "TIME",
		                 "SNOW", "PRESSURE", "HEAT", "DETAILS", "WIND", "VISIBILITY", "WEATHER"]
		for ent, place in self.entity.items():
			self.w = WeatherMan(location=place).controller()
			if ent.upper() == "WEATHER":
				self.data[ent] = self.w
			if ent.upper() == "TEMPERATURE":
				self.data[ent] = self.w['TEMPERATURE']
			if ent.upper() == "RAIN":
				self.data[ent] = self.w['CONDITION']
			if ent.upper() == "CLOUD":
				self.data[ent] = self.w['CONDITION']
			if ent.upper() == "HUMIDITY":
				self.data[ent] = self.w['HUMIDITY']
			if ent.upper() == "SUNSET":
				self.data[ent] = self.w['SUN']['SUNSET']
			if ent.upper() == "SUNRISE":
				self.data[ent] = self.w['SUN']['SUNRISE']
			if ent.upper() == "WIND":
				self.data[ent] = self.w['WIND']
		print(self.data)

	def run(self):
		return self.data


class ChatManager(object):
	def __init__(self, query=None):
		HouseKeeping().__init__()
		self.q = query or "I want to know the weather in bangalore"
		self.resp = dict()
		self.w = None

	def send_input(self):
		self.resp = DoNLPThingy(self.q).run()

	def controller(self):
		self.send_input()
		if self.resp is None:
			print("Something isn't right... ")
		self.e = EntityExtractor(entity=self.resp).run()

	def run(self):
		self.controller()


if __name__ == "__main__":
	c = ChatManager()
	c.run()
