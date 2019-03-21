import unittest
import mock
from mock import patch
from unittest.mock import MagicMock
from includes.exceptions.AppExceptions import DuplicateAssignment
from includes.user.InputProcessor import InputProcessor
from includes.ParkingManager import ParkingManager

class InputProcessorTestCase(unittest.TestCase):
	def setUp(self):
		self.parkingManager = ParkingManager.get_instance()

	def test_user_input_parse(self):
		self.assertEqual(InputProcessor.parse_input("create_parking_lot 6"), 
			("create_parking_lot", ["6"]), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("park KA-01-HH-1234 White"), 
			("park", ["KA-01-HH-1234", "White"]), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("leave 4"), 
			("leave", ["4"]), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("status"), 
			("status", []), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("registration_numbers_for_cars_with_colour White"), 
			("registration_numbers_for_cars_with_colour", ["White"]), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("slot_number_for_registration_number KA-01-HH-3141"), 
			("slot_number_for_registration_number", ["KA-01-HH-3141"]), "Input parsing failed")
		self.assertEqual(InputProcessor.parse_input("registration_numbers_for_cars_with_colour White"), 
			("registration_numbers_for_cars_with_colour", ["White"]), "Input parsing failed")

	def test_process_call_for_manager_with_params(self):
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "park KA-01-HH-1234 White")
		mock.assert_called_with("park")
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "create_parking_lot 6")
		mock.assert_called_with("create_parking_lot")
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "leave 4")
		mock.assert_called_with("leave")
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "status")
		mock.assert_called_with("status")
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "registration_numbers_for_cars_with_colour White")
		mock.assert_called_with("registration_numbers_for_cars_with_colour")
		with patch.object(self.parkingManager, 'process') as mock:
			results = InputProcessor.process(self.parkingManager, "slot_number_for_registration_number KA-01-HH-3141")
		mock.assert_called_with("slot_number_for_registration_number")

	def tearDown(self):
		self.parkingManager.reset()
