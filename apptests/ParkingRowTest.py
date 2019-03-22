import unittest
import random
import multiprocessing
import threading

from includes.entities.Registration import Registration
from includes.exceptions.AppExceptions import ParkingLotFull, NotFound, IncorrectType, DuplicateAssignment, DuplicateCarEntry
from includes.entities.ParkingRow import ParkingRow


class ParkingRowTestCase(unittest.TestCase):
	def setUp(self):
		self.colors = ["White", "Red", "Black", "Green", "Purple", "Pink"]
		self.states = ["KA", "MH", "DL", "GA", "BR", "AR"]
		self.parking_row = ParkingRow(number_of_slots=3, multiprocessing_module=multiprocessing)

	def reset(self):
		self.parking_row.reset()

	def create_new_parking_lot(self, number_of_slots):
		self.parking_row = ParkingRow(number_of_slots=number_of_slots, multiprocessing_module=multiprocessing)

	def populate_with_list(self, list_of_registrations):
		self.reset()
		for registration in list_of_registrations:
			self.parking_row.checkin(Registration(registration_number=registration[0], color=registration[1]))

	def populate_with_thread(self, number_of_vechiles):
		for i in range(number_of_vechiles):
			self.parking_row.checkin(Registration(registration_number=self.get_random_registration_number(), color=random.choice(self.colors)))

	def get_random_registration_number(self):
		return random.choice(self.states)+"-"+str(random.randint(10,99))+"-"+str(random.randint(10,99))+"-"+str(random.randint(1000,9999))

	def populate(self, number_of_vechiles=2):
		self.reset()
		for i in range(number_of_vechiles):
			random_registration_number = random.choice(self.states)+"-"+str(random.randint(10,99))+"-"+str(random.randint(10,99))+"-"+str(random.randint(1000,9999))
			self.parking_row.checkin(Registration(registration_number=random_registration_number, color=random.choice(self.colors)))

	def test_registration_type(self):
		self.assertRaises(IncorrectType, self.parking_row.checkin, ["somegarbage", 420, {'some': 'garbage'}])		

	def test_basic_checkin(self):
		self.assertEqual(self.parking_row.available_slots.get(), 3, 'Wrong available slots')
		self.parking_row.checkin(Registration(registration_number="KA-23-22-33434", color="White"))
		self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple"))
		self.assertEqual(self.parking_row.available_slots.get(), 1, 'Wrong available slots')
		self.assertEqual(self.parking_row.space_matrix[0].registration_number, "KA-23-22-33434", 'Wrong registration number')
		self.assertEqual(self.parking_row.space_matrix[1].registration_number, "BR-5H-95-9999", 'Wrong registration number')

	def test_duplicate_registration_entry(self):
		self.assertEqual(self.parking_row.available_slots.get(), 3, 'Wrong available slots')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="KA-23-22-33434", color="White")), 0, 'Wrong slot')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 1, 'Wrong slot')
		self.assertEqual(self.parking_row.available_slots.get(), 1, 'Wrong available slots')
		self.assertRaises(DuplicateCarEntry, self.parking_row.checkin, Registration(registration_number="BR-5H-95-9999", color="Purple"))
		self.parking_row.checkout(1)
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 1, 'Wrong slot')
		

	def test_checkin_overflow(self):
		self.assertEqual(self.parking_row.available_slots.get(), 3, 'Wrong available slots')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="KA-23-22-33434", color="White")), 0, 'Wrong slot')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 1, 'Wrong slot') 
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")), 2, 'Wrong slot') 
		self.assertRaises(ParkingLotFull, self.parking_row.checkin, Registration(registration_number="KA-LP-79-9999", color="Purple"))
		self.assertEqual(self.parking_row.available_slots.get(), 0, 'Wrong available slots')
		# You know what we are stubborn, we try parking again
		self.assertRaises(ParkingLotFull, self.parking_row.checkin, Registration(registration_number="KA-LP-79-9999", color="Purple"))

	def test_basic_checkout(self):
		self.assertEqual(self.parking_row.available_slots.get(), 3, 'Wrong available slots')
		self.populate(number_of_vechiles=2)
		# Try checking out
		self.assertEqual(self.parking_row.available_slots.get(), 1, 'Wrong available slots')
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		self.assertEqual(self.parking_row.available_slots.get(), 2, 'Wrong available slots')
		# Check the parking spaces if they are available
		self.assertEqual(self.parking_row.space_matrix[0], None, 'Deallocation was not successfull')
		self.assertNotEqual(self.parking_row.space_matrix[1], None, 'A vechile was parked here, where is it now, is it stolen ?')
		self.assertEqual(self.parking_row.space_matrix[2], None, 'Wrong slot filled')

	def test_checkout_twice(self):
		self.populate(number_of_vechiles=2)
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		self.assertRaises(NotFound, self.parking_row.checkout, 0)

	def test_checkin_and_checkout(self):
		self.populate(number_of_vechiles=2)
		# We unpark the card at 0th slot
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		# We park the car and we get the 0th slot
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 0, 'Wrong nearest allocation spot')
		# We park another car and we get the 2nd slot coz 1st and 0th are taken
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="GA-OO-95-3433", color="White")), 2, 'Wrong nearest allocation spot')
		self.assertEqual(self.parking_row.checkout(1), 1, 'Wrong checkout slot output')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="PB-OO-66-1993", color="Blue")), 1, 'Wrong nearest allocation spot')
		self.assertRaises(ParkingLotFull, self.parking_row.checkin, Registration(registration_number="KA-LP-79-9999", color="Purple"))

	def test_dump(self):
		self.populate(number_of_vechiles=2)
		self.assertEqual(len(self.parking_row.dump()), 2, 'Wrong dump')
		self.parking_row.checkout(1)
		self.assertEqual(len(self.parking_row.dump()), 1, 'Wrong dump')
		self.parking_row.checkout(0)
		self.assertEqual(len(self.parking_row.dump()), 0, 'Wrong dump')
		self.populate(number_of_vechiles=3)
		self.assertEqual(len(self.parking_row.dump()), 3, 'Wrong dump')

	def test_find_by_registration(self):
		self.reset()
		self.create_new_parking_lot(number_of_slots=5)
		self.populate_with_list(list_of_registrations=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"]])
		self.assertEqual(self.parking_row.find_by_registration("KH-AA-35-3433")['registration']['registration_number'], "KH-AA-35-3433", "Search by registration number failed")
		self.assertEqual(self.parking_row.find_by_registration("KH-AA-35-3433")['slot'], 2, "Search by registration number failed")
		self.assertEqual(self.parking_row.find_by_registration("KH-BB-35-3433"), None, "Search by registration number failed")
		self.assertEqual(self.parking_row.checkout(2), 2, 'Wrong checkout slot output')
		self.assertEqual(self.parking_row.find_by_registration("KH-AA-35-3433"), None, "Search by registration number failed")

	def test_find_by_color(self):
		self.reset()
		self.create_new_parking_lot(number_of_slots=4)
		self.populate_with_list(list_of_registrations=[["BR-5H-95-9999", "Purple"], ["GA-OO-95-3433", "White"], ["KH-AA-35-3433", "Black"], ["KA-PA-35-3433", "Black"]])
		self.assertEqual(len(self.parking_row.find_by_color("Black")), 2, "Search by color failed")
		self.assertEqual(self.parking_row.find_by_color("Black")[0]['slot'], 2, "Search by color failed")
		self.assertEqual(self.parking_row.find_by_color("Black")[1]['slot'], 3, "Search by color failed")
		self.assertEqual(self.parking_row.find_by_color("Black")[1]['registration']['registration_number'], "KA-PA-35-3433", "Search by color failed")
		self.assertEqual(len(self.parking_row.find_by_color("Red")), 0, "Search by color failed")
		self.assertEqual(len(self.parking_row.find_by_color("White")), 1, "Search by color failed")
		self.assertEqual(self.parking_row.find_by_color("White")[0]['registration']['registration_number'], "GA-OO-95-3433", "Search by color failed")

	def test_multiple_threads(self):
		self.reset()
		self.create_new_parking_lot(number_of_slots=100)
		thread1 = multiprocessing.Process(target = self.populate_with_thread, args = [25]) 
		thread2 = multiprocessing.Process(target = self.populate_with_thread, args = [20]) 
		thread3 = multiprocessing.Process(target = self.populate_with_thread, args = [15]) 
		thread4 = multiprocessing.Process(target = self.populate_with_thread, args = [30]) 
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		thread1.join()
		thread2.join()
		thread3.join()
		thread4.join()
		self.assertEqual(self.parking_row.available_slots.get(), 10, "Program not threadsafe")
		self.reset()
		self.create_new_parking_lot(number_of_slots=50)
		thread1 = multiprocessing.Process(target = self.populate_with_thread, args = [8]) 
		thread2 = multiprocessing.Process(target = self.populate_with_thread, args = [4]) 
		thread3 = multiprocessing.Process(target = self.populate_with_thread, args = [6]) 
		thread4 = multiprocessing.Process(target = self.populate_with_thread, args = [9]) 
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		thread1.join()
		thread2.join()
		thread3.join()
		thread4.join()
		self.assertEqual(self.parking_row.available_slots.get(), 23, "Program not threadsafe")

