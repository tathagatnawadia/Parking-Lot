from .Vechile import Vechile
from .Dumper import Dumper
import datetime

class Registration(Dumper, Vechile):
	delimiter = "-"
	def __init__(self, registration_number, color):
		self.segments = registration_number.split(Registration.delimiter)
		self.registration_number = registration_number
		self.checkin_time = str(datetime.datetime.now())
		Vechile.__init__(self, color=color)

	def dispose(self):
		self.segments = None

	def dump(self):
		return vars(self)

