import unittest
import random

from apptests.RegistrationTest import RegistrationTestCase
from apptests.ParkingRowTest import ParkingRowTestCase
from apptests.ParkingLotTest import ParkingLotTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegistrationTestCase('test_segment_size'))
    suite.addTest(RegistrationTestCase('test_registration_string'))

    suite.addTest(ParkingRowTestCase('test_basic_checkin'))
    suite.addTest(ParkingRowTestCase('test_checkin_overflow'))
    suite.addTest(ParkingRowTestCase('test_basic_checkout'))
    suite.addTest(ParkingRowTestCase('test_checkout_twice'))
    suite.addTest(ParkingRowTestCase('test_checkin_and_checkout'))
    suite.addTest(ParkingRowTestCase('test_registration_type'))
    suite.addTest(ParkingRowTestCase('test_dump'))
    suite.addTest(ParkingRowTestCase('test_find_by_registration'))
    suite.addTest(ParkingRowTestCase('test_find_by_color'))
    suite.addTest(ParkingRowTestCase('test_multiple_threads'))

    suite.addTest(ParkingLotTestCase('test_assignment_of_parking_lot'))
    suite.addTest(ParkingLotTestCase('test_duplicate_assignment'))
    suite.addTest(ParkingLotTestCase('test_park_vechile'))
    suite.addTest(ParkingLotTestCase('test_parking_full'))
    suite.addTest(ParkingLotTestCase('test_leave_vechile'))
    suite.addTest(ParkingLotTestCase('test_leave_from_already_empty'))
    suite.addTest(ParkingLotTestCase('test_park_and_leave'))
    suite.addTest(ParkingLotTestCase('test_slot_numbers_for_cars_with_colour'))
    suite.addTest(ParkingLotTestCase('test_registration_numbers_for_cars_with_colour'))
    suite.addTest(ParkingLotTestCase('test_slot_number_for_registration_number'))
    
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())