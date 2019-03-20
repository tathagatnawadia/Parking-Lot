import unittest
import random

from includes.Registration import Registration
from includes.AppExceptions import ParkingLotFull, NotFound, IncorrectType
from main import ParkingRow


class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.registration = Registration(registration_number="KA-23-22-33434", color="White")

    def test_segment_size(self):
        self.assertEqual(len(self.registration.segments), 4,
                         'incorrect segment size')

    def test_registration_string(self):
        self.assertEqual(self.registration.registration_number, "KA-23-22-33434",
                         '')
    def tearDown(self):
        self.registration.dispose()


class ParkingRowTestCase(unittest.TestCase):
	def setUp(self):
		self.colors = ["White", "Red", "Black", "Green", "Purple", "Pink"]
		self.states = ["KA", "MH", "DL", "GA", "BR", "AR"]
		self.parking_row = ParkingRow(3)

	def populate(self, number_of_vechiles=2):
		# This function autopopulates number_of_vechiles in the parking lot
		for i in range(number_of_vechiles):
			random_registration_number = random.choice(self.states)+"-"+str(random.randint(10,99))+"-"+str(random.randint(10,99))+"-"+str(random.randint(1000,9999))
			self.parking_row.checkin(Registration(registration_number=random_registration_number, color=random.choice(self.colors)))

	def test_registration_type(self):
		self.assertRaises(IncorrectType, self.parking_row.checkin, ["somegarbage", 420, {'some': 'garbage'}])		

	def test_basic_checkin(self):
		self.assertEqual(self.parking_row.available_slots, 3, 'Wrong available slots')
		self.parking_row.checkin(Registration(registration_number="KA-23-22-33434", color="White"))
		self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple"))
		self.assertEqual(self.parking_row.available_slots, 1, 'Wrong available slots')
		self.assertEqual(self.parking_row.space_matrix[0].registration_number, "KA-23-22-33434", 'Wrong registration number')
		self.assertEqual(self.parking_row.space_matrix[1].registration_number, "BR-5H-95-9999", 'Wrong registration number')

	def test_checkin_overflow(self):
		self.assertEqual(self.parking_row.available_slots, 3, 'Wrong available slots')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="KA-23-22-33434", color="White")), 0, 'Wrong slot')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 1, 'Wrong slot') 
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="MH-YY-95-9999", color="Purple")), 2, 'Wrong slot') 
		self.assertRaises(ParkingLotFull, self.parking_row.checkin, Registration(registration_number="KA-LP-79-9999", color="Purple"))
		self.assertEqual(self.parking_row.available_slots, 0, 'Wrong available slots')
		# You know what we are stubborn, we try parking again
		self.assertRaises(ParkingLotFull, self.parking_row.checkin, Registration(registration_number="KA-LP-79-9999", color="Purple"))

	def test_basic_checkout(self):
		self.assertEqual(self.parking_row.available_slots, 3, 'Wrong available slots')
		self.populate(number_of_vechiles=2)
		# Try checking out
		self.assertEqual(self.parking_row.available_slots, 1, 'Wrong available slots')
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		self.assertEqual(self.parking_row.available_slots, 2, 'Wrong available slots')
		# Check the parking spaces if they are available
		self.assertEqual(self.parking_row.space_matrix[0], None, 'Deallocation was not successfull')
		self.assertNotEqual(self.parking_row.space_matrix[1], None, 'A vechile was parked here, where is it now, is it stolen ?')
		self.assertEqual(self.parking_row.space_matrix[2], None, 'Wrong slot filled')

	def test_checkout_twice(self):
		self.populate(number_of_vechiles=2)
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		self.assertRaises(NotFound, self.parking_row.checkout, 0)

	def test_checkin_checkout(self):
		self.populate(number_of_vechiles=2)
		self.assertEqual(self.parking_row.checkout(0), 0, 'Wrong checkout slot output')
		self.assertEqual(self.parking_row.checkin(Registration(registration_number="BR-5H-95-9999", color="Purple")), 0, 'Wrong nearest allocation spot')
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

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegistrationTestCase('test_segment_size'))
    suite.addTest(RegistrationTestCase('test_registration_string'))


    suite.addTest(ParkingRowTestCase('test_basic_checkin'))
    suite.addTest(ParkingRowTestCase('test_checkin_overflow'))
    suite.addTest(ParkingRowTestCase('test_basic_checkout'))
    suite.addTest(ParkingRowTestCase('test_checkout_twice'))
    suite.addTest(ParkingRowTestCase('test_checkin_checkout'))
    suite.addTest(ParkingRowTestCase('test_registration_type'))
    suite.addTest(ParkingRowTestCase('test_dump'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())