import datetime
import abc
import sys

class Dumper(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def dump(self):
		raise Exception('Compulsary implementation of dump method which dumps all data in the object')

class Vechile():
	def __init__(self, color=None):
		self.color = color 
		self.capacity = None
		self.company = None
		self.model = None
		self.type_of_vechile = "SUV"


class Registration(Dumper, Vechile):
	delimiter = "-"
	def __init__(self, registration_number, color):
		self.segments = registration_number.split(Registration.delimiter)
		self.registration_number = registration_number
		self.checkin_time = str(datetime.datetime.now())
		Vechile.__init__(self, color=color)

	def dump(self):
		return vars(self)

	def dispose(self):
		self.segments = None


s = Registration(registration_number="KA-23-22-33434", color="White")
print(s.dump())