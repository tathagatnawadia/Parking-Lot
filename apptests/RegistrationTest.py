import unittest
from includes.entities.Registration import Registration

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