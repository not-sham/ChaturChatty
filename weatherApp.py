from weather import Weather, Unit


class WeatherMan(object):
	def __init__(self, location="Bangalore", forecast=False, lat_lng=None, zip_code=None):
		self.w = Weather(unit=Unit.CELSIUS)
		self.loc = location
		self.zc = zip_code
		self.lat_lng = lat_lng
		self.info = None
		self.forecast = forecast
		self.resp = dict()

	def lookup_by_zip_code(self):
		self.info = self.w.lookup(self.zc)

	def lookup_by_lat_long(self):
		lat, lng = self.lat_lng[0], self.lat_lng[1]
		self.info = self.w.lookup_by_latlng(lat=lat, lng=lng)

	def lookup_by_location(self):
		self.info = self.w.lookup_by_location(location=self.loc)

	def extract_params(self):
		self.resp = {
			"CONDITION": self.info.condition.text,
			"DESCRIPTION": self.info.description,
			"HUMIDITY": self.info.atmosphere.get('humidity'),
			"PRESSURE": self.info.atmosphere.get('pressure'),
			"SUN": {
				"SUNSET": self.info.astronomy.get('sunset'),
				"SUNRISE": self.info.astronomy.get('sunrise'),
			},
			"TEMPERATURE": self.info.condition.temp,
			"UNITS": {
				"DISTANCE": self.info.units.distance,
				"PRESSURE": self.info.units.pressure,
				"SPEED": self.info.units.speed,
				"TEMPERATURE": self.info.units.temperature
			},
			"WIND": {
				"CHILL": self.info.wind.chill,
				"DIRECTION": self.info.wind.direction,
				"SPEED": self.info.wind.speed
			}
		}

	def forecast_params(self):
		if self.forecast is True:
			for f in self.info.forecast:
				d = dict()
				d['day'] = f.day
				d['high'] = f.high
				d['low'] = f.low
				d['text'] = f.text
				self.resp[f.date] = d

	def controller(self):
		if self.loc:
			self.lookup_by_location()
		elif self.lat_lng:
			self.lookup_by_lat_long()
		elif self.zc:
			self.lookup_by_zip_code()
		else:
			pass
		if self.info:
			self.extract_params()
			self.forecast_params()
		return self.resp


if __name__ == "__main__":
	w = WeatherMan(location="Annapolis")
	print(w.controller())
