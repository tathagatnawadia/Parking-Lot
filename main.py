import datetime
import abc
import sys


class ParkingLotFull(Exception):
	pass
class NotFound(Exception):
	pass
class ExceedsLimit(Exception):
	pass

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

	def dispose(self):
		self.segments = None

	def dump(self):
		return vars(self)




class ParkingRow():
	def __init__(self, number_of_slots):
		self.number_of_slots = number_of_slots
		self.available_slots = number_of_slots
		self.space_matrix = [None for i in range(number_of_slots)]

	def reset(self):
		self.available_slots = self.number_of_slots
		self.space_matrix = [None for i in range(number_of_slots)]

	def allocate(self, registration, slot_number):
		self.available_slots -= 1
		self.space_matrix[slot_number] = registration

	def deallocate(self, slot_number):
		self.available_slots += 1
		self.space_matrix[slot_number] = None

	def find_empty(self):
		for slot_number, slot_candidate in enumerate(self.space_matrix):
			if slot_candidate == None:
				return slot_number
		return None

	def find_by_slot(self, slot_number):
		return self.space_matrix[slot_number]

	def checkin(self, registration):
		if self.available_slots == 0:
			raise ParkingLotFull('Sorry, parking lot is full.')
		first_empty_slot = self.find_empty()
		self.allocate(registration, first_empty_slot)
		return first_empty_slot

	def checkout(self, slot_number):
		if slot_number >= self.number_of_slots:
			raise ExceedsLimit('Slot number exceeds limit.')
		if self.find_by_slot(slot_number) == None:
			raise NotFound('Slot is empty.')
		else:
			self.deallocate(slot_number)
		return slot_number


# s = Registration(registration_number="KA-23-22-33434", color="White")
# p = ParkingRow(3)
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkout(1))

# print(p.space_matrix)