import unittest
import random

from apptests.RegistrationTest import RegistrationTestCase
from apptests.ParkingRowTest import ParkingRowTestCase
from apptests.ParkingLotTest import ParkingLotTestCase
from apptests.InputProcessorTest import InputProcessorTestCase
from apptests.ParkingManagerTest import ParkingManagerTestCase


def suite():
    suite = unittest.TestSuite()

    suite.addTest(RegistrationTestCase('test_segment_size'))
    suite.addTest(RegistrationTestCase('test_registration_string'))

    suite.addTest(ParkingRowTestCase('test_basic_checkin'))
    suite.addTest(ParkingRowTestCase('test_duplicate_registration_entry'))
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

    suite.addTest(InputProcessorTestCase('test_user_input_parse'))
    suite.addTest(InputProcessorTestCase('test_process_call_for_manager_with_params'))

    suite.addTest(ParkingManagerTestCase('test_making_another_parking_manager'))
    suite.addTest(ParkingManagerTestCase('test_creating_parking_lots_func'))
    suite.addTest(ParkingManagerTestCase('test_user_commands'))
    suite.addTest(ParkingManagerTestCase('test_sanity_usecase_1'))
    suite.addTest(ParkingManagerTestCase('test_sanity_usecase_2'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())