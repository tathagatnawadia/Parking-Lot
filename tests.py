import unittest
from main import Registration

class RegistrationTestCase(unittest.TestCase):
    def setUp(self):
        self.registration = Registration("KA-23-22-33434")

    def test_segment_size(self):
        self.assertEqual(len(self.registration.segments), 4,
                         'incorrect segment size')

    def test_registration_string(self):
        self.assertEqual(self.registration.registration_number, "KA-23-22-33434",
                         'wrong size after resize')
    def tearDown(self):
        self.registration.dispose()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegistrationTestCase('test_segment_size'))
    suite.addTest(RegistrationTestCase('test_registration_string'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())