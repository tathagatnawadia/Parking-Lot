import multiprocessing

from includes.exceptions.AppExceptions import ParkingLotFull, NotFound, DuplicateAssignment
from includes.log.AppLogger import *
from includes.interfaces.Dumper import Dumper
from includes.configs.Defaults import Default, Action
from includes.configs.Messages import Message
from includes.helpers.ParamsHelper import ParamsHelper
from includes.entities.Registration import Registration
from includes.entities.ParkingRow import ParkingRow


class ParkingLot(Dumper):
	def __init__(self):
		self.reset()

	def reset(self):
		self.incharge = Default.ADMIN
		self.timings = Default.TIMING
		self.ownership = Default.OWNER
		self.parking = None

	def assign_parking_lot(self, number_of_slots):
		if self.parking == None:
			self.parking = ParkingRow(number_of_slots=number_of_slots, multiprocessing_module=multiprocessing)
			return Message.PARKINGLOT_CREATION_SUCCESS % (self.parking.number_of_slots)
		else:
			raise DuplicateAssignment('Contact the administrator')

	def checkin(self, params):
		registration_number, color = ParamsHelper.getParams(Action.PARK, params)
		try:
			return Message.ALLOCATION_SUCCESS % (self.parking.checkin(Registration(registration_number, color)) + 1)
		except ParkingLotFull:
			return Message.ALLOCATION_FAILURE_SLOTFULL

	def checkout(self, params):
		slot_number = ParamsHelper.getParams(Action.LEAVE, params)
		try:
			return Message.DEALLOCATION_SUCCESS % (self.parking.checkout(slot_number - 1) + 1)
		except NotFound:
			return Message.NOT_FOUND

	def status(self, params):
		output = []
		output.append(Message.PARKINGLOT_STATUS_HEADER)
		for parking in self.dump():
			output.append(str(parking["slot"] + 1) + "\t" + parking["registration"]["registration_number"] + "\t " + parking["registration"]["color"])
		return Default.NEWLINE.join(map(str, output))

	def slot_numbers_for_cars_with_colour(self, params):
		color = ParamsHelper.getParams(Action.SEARCH_BY_COLOR, params)
		results = self.parking.find_by_color([color])
		if len(results) != 0:
			output = [parked["slot"] + 1 for parked in results]
			return Default.COMMA_SEPERATOR.join(map(str, output))
		else:
			return Message.NOT_FOUND

	def registration_numbers_for_cars_with_colour(self, params):
		color = ParamsHelper.getParams(Action.SEARCH_BY_COLOR, params)
		results = self.parking.find_by_color([color])

		if len(results) != 0:
			output = [parked["registration"]["registration_number"] for parked in results]
			return Default.COMMA_SEPERATOR.join(map(str, output))
		else:
			return Message.NOT_FOUND

	def slot_number_for_registration_number(self, params):
		registration_number = ParamsHelper.getParams(Action.SEARCH_BY_REGISTRATION, params)
		result = self.parking.find_by_registration(registration_number)
		if result != None:
			return str(result["slot"] + 1)
		else:
			return Message.NOT_FOUND

	def dump(self):
		return self.parking.dump()
