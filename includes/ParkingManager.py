from includes.exceptions.AppExceptions import UnknwnCommand
from includes.log.AppLogger import *
from includes.interfaces.Processor import Processor
from includes.configs.Defaults import Action
from includes.configs.UserCommands import UserCommands
from includes.helpers.ParamsHelper import ParamsHelper
from includes.usecases.ParkingLot import ParkingLot

"""
The manager of the parking lots
	- Singleton class created during startup of the program
	- What can it do : It can create and store multiple levels of parking lots (Eg. 3 parking lots of 5 cars = 15 cars :) )
	- It also maps the commands to the function calls
	- Adding a new command will be as easy as adding the function at the class ParkingLot and the mapping it here in command
"""
class ParkingManager(Processor):
	__instance = None
	__parkingLotCollections = None
	@staticmethod
	def get_instance():
		if ParkingManager.__instance == None:
			ParkingManager()
		return ParkingManager.__instance

	@staticmethod
	def reset():
		ParkingManager.__instance = None
		ParkingManager.__parkingLotCollections = None		

	def __init__(self):
		if ParkingManager.__instance != None:
			raise Exception("Singleton class should not be instanitated more than once.")
		else:
			ParkingManager.__instance = self
			ParkingManager.__parkingLotCollections = []
			ParkingManager.command = {}
			ParkingManager.command[UserCommands['CREATE_PARKING_LOT']] = self.add_parking_slot

	def add_parking_slot(self, params):
		# Here I have added support of having multiple parking slots
		number_of_slots = ParamsHelper.getParams(Action.CREATE_PARKING_LOT, params)
		fresh_parking_lot = ParkingLot()
		self.__parkingLotCollections.append(fresh_parking_lot)
		parking_lot_code = len(self.__parkingLotCollections)-1
		self.command[parking_lot_code] = {
		  	UserCommands['PARK']: 						 	self.__parkingLotCollections[parking_lot_code].checkin,
		  	UserCommands['LEAVE']: 							self.__parkingLotCollections[parking_lot_code].checkout,
		  	UserCommands['GET_REGISTRATIONS_FROM_COLOR']: 	self.__parkingLotCollections[parking_lot_code].registration_numbers_for_cars_with_colour,
		  	UserCommands['GET_SLOTS_FROM_COLOR']:		 	self.__parkingLotCollections[parking_lot_code].slot_numbers_for_cars_with_colour,
		  	UserCommands['GET_SLOT_FROM_REGISTRATION']: 	self.__parkingLotCollections[parking_lot_code].slot_number_for_registration_number,
		  	UserCommands['STATUS']: 						self.__parkingLotCollections[parking_lot_code].status,
		}
		return fresh_parking_lot.assign_parking_lot(number_of_slots)

	def process(self, command, parking_lot_code=0):
		# process commands like - park, status, leave and so on
		if command in self.command.keys():
			return self.command[command]
		if command in self.command[parking_lot_code].keys(): 
			return self.command[parking_lot_code][command]
		raise UnknwnCommand("Unrecognizable command.")