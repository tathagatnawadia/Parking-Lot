from includes.entities.Vechile import Vechile
from includes.interfaces.Dumper import Dumper
from includes.configs.Defaults import Default
import datetime

class Registration(Dumper, Vechile):
	def __init__(self, registration_number, color):
		self.segments = registration_number.split(Default.REGISTRATION_DELIMITER)
		self.registration_number = registration_number
		self.checkin_time = str(datetime.datetime.now())
		Vechile.__init__(self, color=color)

	def dispose(self):
		self.segments = None

	def dump(self):
		return vars(self)

