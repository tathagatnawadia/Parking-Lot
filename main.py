import datetime
import sys
from includes.AppExceptions import ParkingLotFull, NotFound, ExceedsLimit, IncorrectType
from includes.Registration import Registration
from includes.Dumper import Dumper

class ParkingRow(Dumper):
	def __init__(self, number_of_slots):
		self.number_of_slots = number_of_slots
		self.available_slots = number_of_slots
		self.space_matrix = [None for i in range(number_of_slots)]

	def reset(self):
		self.available_slots = self.number_of_slots
		self.space_matrix = [None for i in range(self.number_of_slots)]

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
		if not isinstance(registration, Registration):
			raise IncorrectType('Correct type : Registration')

		first_empty_slot = self.find_empty()
		self.allocate(registration, first_empty_slot)
		return first_empty_slot

	def checkout(self, slot_number):
		if slot_number >= self.number_of_slots:
			raise ExceedsLimit('Slot number exceeds limit.')
		if self.find_by_slot(slot_number) == None:
			raise NotFound('Slot is empty.')
		
		self.deallocate(slot_number)
		return slot_number

	def find_by_registration(self, registration_number):
		for slot_number, slot_candidate in enumerate(self.space_matrix):
			if slot_candidate != None and slot_candidate.registration_number == registration_number:
				return {"registration" : slot_candidate.dump(), "slot" : slot_number}
		return None

	def find_by_color(self, colors=[]):
		parking_lot_vechiles = []
		for slot_number, slot_candidate in enumerate(self.space_matrix):
			if slot_candidate != None and slot_candidate.color in colors:
				parking_lot_vechiles.append({"registration" : slot_candidate.dump(), "slot" : slot_number})
		return parking_lot_vechiles

	def dump(self):
		result = [{ "registration": slot_candidate.dump(), "slot": slot_number} for slot_number, slot_candidate in enumerate(self.space_matrix) if slot_candidate != None]
		return result


# s = Registration(registration_number="KA-23-22-33434", color="White")
# p = ParkingRow(3)
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")))
# print(p.checkout(1))

# print(p.find_by_registration("MH-YY-95-9999"))



