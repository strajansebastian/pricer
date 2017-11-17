class Vehicle(object):
	def __init__(self, brand, model, year, price):
		self._brand = brand
		self._model = model
		self._year = year
		self._price = price

	@property
	def brand(self):
		return self._brand

	@brand.setter
	def brand(self, value):
		self._brand = value

	@property
	def model(self):
		return self._model

	@model.setter
	def brand(self, value):
		self._model = value

	@property
	def year(self):
		return self._year

	@year.setter
	def brand(self, value):
		self._year = value

	@property
	def price(self):
		return self._price

	@price.setter
	def brand(self, value):
		self._price = value


