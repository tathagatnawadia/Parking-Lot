from includes.configs.Defaults import Default

class Vechile():
	def __init__(self, color=None):
		self.color = color 
		self.capacity = None
		self.company = None
		self.model = None
		self.type_of_vechile = Default.VECHILE_TYPE
