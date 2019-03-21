import unittest
from includes.exceptions.AppExceptions import DuplicateAssignment
from includes.usecases.ParkingLot import ParkingLot

class ParkingLotTestCase(unittest.TestCase):
	def setUp(self):
		self.parking_lot = ParkingLot()

	def helper_populate_checkin(self, list_of_vechiles):
		for vechile in list_of_vechiles:
			self.parking_lot.checkin(vechile)

	def test_assignment_of_parking_lot(self):
		self.assertEqual(self.parking_lot.assign_parking_lot(5), "Created a parking lot with 5 slots", "Creation of parking lot failed")

	def test_duplicate_assignment(self):
		self.assertEqual(self.parking_lot.assign_parking_lot(100000), "Created a parking lot with 100000 slots", "Creation of parking lot failed")
		self.assertRaises(DuplicateAssignment, self.parking_lot.assign_parking_lot, 15)

	def test_park_vechile(self):
		self.parking_lot.assign_parking_lot(4)
		self.assertEqual(self.parking_lot.checkin(["KA-01-HH-1234", "White"]), "Allocated slot number: 1", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["BR-01-HH-1234", "White"]), "Allocated slot number: 2", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["MH-01-HH-1234", "White"]), "Allocated slot number: 3", "Parking failed")

	def test_parking_full(self):
		self.parking_lot.assign_parking_lot(4)
		self.helper_populate_checkin(list_of_vechiles=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"]])
		self.assertEqual(self.parking_lot.checkin(["MH-01-HH-1234", "White"]), "Allocated slot number: 4", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["GA-01-HH-1234", "White"]), "Sorry, parking lot is full", "Parking failed")

	def test_leave_vechile(self):
		self.parking_lot.assign_parking_lot(5)
		self.helper_populate_checkin(list_of_vechiles=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"],
			["GA-01-HH-1234", "White"]])
		self.assertEqual(self.parking_lot.checkout("1"), "Slot number 1 is free", "Leaving failed")
		self.assertEqual(self.parking_lot.checkout("4"), "Slot number 4 is free", "Leaving failed")
		self.assertEqual(self.parking_lot.parking.space_matrix[0], None, "Data Corrupted")
		self.assertEqual(self.parking_lot.parking.space_matrix[3], None, "Data Corrupted")
		self.assertNotEqual(self.parking_lot.parking.space_matrix[1], None, "Data Corrupted")
		self.assertNotEqual(self.parking_lot.parking.space_matrix[2], None, "Data Corrupted")

	def test_leave_from_already_empty(self):
		self.parking_lot.assign_parking_lot(5)
		self.helper_populate_checkin(list_of_vechiles=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"],
			["GA-01-HH-1234", "White"]])
		self.assertEqual(self.parking_lot.checkout(["3"]), "Slot number 3 is free", "Leaving failed")
		self.assertEqual(self.parking_lot.checkout(["3"]), "Not Found", "Leaving failed")

	def test_park_and_leave(self):
		self.parking_lot.assign_parking_lot(5)
		self.helper_populate_checkin(list_of_vechiles=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"],
			["GA-01-HH-1234", "White"]])
		self.assertEqual(self.parking_lot.checkout(["3"]), "Slot number 3 is free", "Leaving failed")
		self.assertEqual(self.parking_lot.checkout(["1"]), "Slot number 1 is free", "Leaving failed")
		self.assertEqual(self.parking_lot.checkin(["MH-99-GH-1234", "Black"]), "Allocated slot number: 1", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["KA-99-GH-1234", "Blue"]), "Allocated slot number: 3", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["BR-88-72-3454", "White"]), "Allocated slot number: 5", "Parking failed")
		self.assertEqual(self.parking_lot.checkin(["KA-99-38-1884", "Black"]), "Sorry, parking lot is full", "Parking failed")


	def test_slot_numbers_for_cars_with_colour(self):
		self.test_park_and_leave()
		self.assertEqual(self.parking_lot.slot_numbers_for_cars_with_colour(["White"]), "2, 4, 5", "Search for color failed")
		self.assertEqual(self.parking_lot.slot_numbers_for_cars_with_colour(["Black"]), "1", "Search for color failed")
		self.assertEqual(self.parking_lot.slot_numbers_for_cars_with_colour(["Purple"]), "Not Found", "Search for color failed")

	def test_registration_numbers_for_cars_with_colour(self):
		self.test_park_and_leave()
		self.assertEqual(self.parking_lot.registration_numbers_for_cars_with_colour(["White"]), 
				"GA-OO-95-3433, GA-01-HH-1234, BR-88-72-3454", "Search for color failed")
		self.assertEqual(self.parking_lot.registration_numbers_for_cars_with_colour(["Black"]), 
				"MH-99-GH-1234", "Search for color failed")
		self.assertEqual(self.parking_lot.registration_numbers_for_cars_with_colour(["Purple"]), 
				"Not Found", "Search for color failed")

	def test_slot_number_for_registration_number(self):
		self.test_park_and_leave()
		self.assertEqual(self.parking_lot.slot_number_for_registration_number(["KA-99-38-1884"]), "Not Found", "Search for registration failed")
		self.assertEqual(self.parking_lot.slot_number_for_registration_number(["BR-88-72-3454"]), "5", "Search for registration failed")
		self.assertEqual(self.parking_lot.slot_number_for_registration_number(["KA-99-GH-1234"]), "3", "Search for registration failed")
		self.assertEqual(self.parking_lot.slot_number_for_registration_number(["GA-OO-95-3433"]), "2", "Search for registration failed")
