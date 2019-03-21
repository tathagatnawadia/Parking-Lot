import unittest
from includes.ParkingManager import ParkingManager
from includes.exceptions.AppExceptions import UnknwnCommand

class ParkingManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.parkingManager = ParkingManager.get_instance()

    def test_making_another_parking_manager(self):
        self.assertRaises(Exception, ParkingManager)

    def test_creating_parking_lots_func(self):
        self.assertEqual(self.parkingManager.process("create_parking_lot"),
            self.parkingManager.add_parking_slot, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("create_parking_lot")(["4"]),
            "Created a parking lot with 4 slots", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("create_parking_lot")(["69"]),
            "Created a parking lot with 69 slots", 'ParkingLot creation failed from manager')
        parkingCollection = ParkingManager._ParkingManager__parkingLotCollections
        self.assertEqual(parkingCollection[0].parking.number_of_slots,
            4, 'Incorrect number of slots')
        self.assertEqual(parkingCollection[0].parking.available_slots.get(),
            4, 'Incorrect number of slots')
        self.assertEqual(parkingCollection[1].parking.number_of_slots,
            69, 'Incorrect number of slots')
        self.assertEqual(parkingCollection[1].parking.available_slots.get(),
            69, 'Incorrect number of slots')

    def test_user_commands(self):
        parkingCollection = ParkingManager._ParkingManager__parkingLotCollections
        self.assertRaises(UnknwnCommand, self.parkingManager.process, "create_my_boat")
        self.assertEqual(self.parkingManager.process("park"),
            parkingCollection[0].checkin, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("leave"),
            parkingCollection[0].checkout, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("status"),
            parkingCollection[0].status, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("registration_numbers_for_cars_with_colour"),
            parkingCollection[0].registration_numbers_for_cars_with_colour, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour"),
            parkingCollection[0].slot_numbers_for_cars_with_colour, 'Wrong/Invalid function pointer')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number"),
            parkingCollection[0].slot_number_for_registration_number, 'Wrong/Invalid function pointer')
        self.assertRaises(UnknwnCommand, self.parkingManager.process, "fly_my_horse")


    def test_sanity_usecase_1(self):
        self.assertEqual(self.parkingManager.process("park")(["KA-01-HH-1234", "White"]),
            "Allocated slot number: 1", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park")(["KA-01-HH-9999", "White"]),
            "Allocated slot number: 2", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park")(["KA-01-HH-3141", "Black"]),
            "Allocated slot number: 3", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("leave")(["2"]),
            "Slot number 2 is free", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park")(["KA-01-HH-9933", "Black"]),
            "Allocated slot number: 2", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("registration_numbers_for_cars_with_colour")(["Black"]),
            "KA-01-HH-9933, KA-01-HH-3141", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number")(["KA-01-HH-9999"]),
            "Not Found", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number")(["KA-01-HH-3141"]),
            "3", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour")(["White"]),
            "1", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour")(["Green"]),
            "Not Found", 'ParkingLot creation failed from manager')

    def test_sanity_usecase_2(self):
        self.assertEqual(self.parkingManager.process("park", parking_lot_code=1)(["KA-01-HH-1234", "Brown"]),
            "Allocated slot number: 1", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park", parking_lot_code=1)(["KA-01-HH-9999", "Brown"]),
            "Allocated slot number: 2", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park", parking_lot_code=1)(["KA-01-HH-3141", "Blue"]),
            "Allocated slot number: 3", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("leave", parking_lot_code=1)(["2"]),
            "Slot number 2 is free", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("park", parking_lot_code=1)(["KA-01-HH-9933", "Blue"]),
            "Allocated slot number: 2", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("registration_numbers_for_cars_with_colour", parking_lot_code=1)(["Blue"]),
            "KA-01-HH-9933, KA-01-HH-3141", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number", parking_lot_code=1)(["KA-01-HH-9999"]),
            "Not Found", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number", parking_lot_code=1)(["KA-01-HH-3141"]),
            "3", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour", parking_lot_code=1)(["Brown"]),
            "1", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour", parking_lot_code=1)(["Green"]),
            "Not Found", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("registration_numbers_for_cars_with_colour")(["Black"]),
            "KA-01-HH-9933, KA-01-HH-3141", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number")(["KA-01-HH-9999"]),
            "Not Found", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_number_for_registration_number")(["KA-01-HH-3141"]),
            "3", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour")(["White"]),
            "1", 'ParkingLot creation failed from manager')
        self.assertEqual(self.parkingManager.process("slot_numbers_for_cars_with_colour")(["Green"]),
            "Not Found", 'ParkingLot creation failed from manager')


