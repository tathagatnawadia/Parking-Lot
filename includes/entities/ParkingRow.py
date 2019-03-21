from includes.exceptions.AppExceptions import ParkingLotFull, NotFound, ExceedsLimit, IncorrectType
from includes.log.AppLogger import *
from includes.interfaces.Dumper import Dumper
from includes.configs.Defaults import Action
from includes.configs.Messages import Message
from includes.entities.Registration import Registration

class ParkingRow(Dumper):
	def __init__(self, number_of_slots, multiprocessing_module):
		self.number_of_slots = number_of_slots
		self.manager = multiprocessing_module.Manager()
		self.lock = multiprocessing_module.Lock()
		self.available_slots = self.manager.Value('available_slots', number_of_slots)
		self.space_matrix = self.manager.list([None for i in range(number_of_slots)])

	def reset(self):
		logging.warn('Reseting ParkingRow')
		self.available_slots = self.manager.Value('available_slots', self.number_of_slots)
		self.space_matrix = [None for i in range(self.number_of_slots)]

	def allocate(self, registration, slot_number):
		self.available_slots.set(self.available_slots.get() - 1)
		self.space_matrix[slot_number] = registration

	def deallocate(self, slot_number):
		self.available_slots.set(self.available_slots.get() + 1)
		self.space_matrix[slot_number] = None

	def get_next_empty(self):
		first_empty_slot = None
		for slot_number, slot_candidate in enumerate(self.space_matrix):
			if slot_candidate == None:
				first_empty_slot = slot_number
				break
		return first_empty_slot

	def get_by_slot(self, slot_number):
		return self.space_matrix[slot_number]

	def checkin(self, registration):
		if self.available_slots.get() == 0:
			logging.warn('Parking lot full '+str(registration.dump()))
			raise ParkingLotFull('Sorry, parking lot is full.')
		if not isinstance(registration, Registration):
			logging.error('Incorrect type of registration used')
			raise IncorrectType('Correct type : Registration')

		self.lock.acquire()
		try:
			first_empty_slot = self.get_next_empty()
			self.allocate(registration, first_empty_slot)
		finally:
			self.lock.release()
		logging.info('Success checkin '+str(registration.dump())+ " " + str(first_empty_slot))
		return first_empty_slot

	def checkout(self, slot_number):
		if slot_number >= self.number_of_slots:
			raise ExceedsLimit('Slot number exceeds limit.')
		if self.get_by_slot(slot_number) == None:
			raise NotFound('Slot is empty.')

		self.lock.acquire()
		try:
			self.deallocate(slot_number)
		finally:
			self.lock.release()

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
		return [{ "registration": slot_candidate.dump(), "slot": slot_number} for slot_number, slot_candidate in enumerate(self.space_matrix) if slot_candidate != None]
