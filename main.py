class Registration():
	delimiter = "-"
	def __init__(self, registration_number):
		self.segments = registration_number.split(Registration.delimiter)
		self.registration_number = registration_number
	def dispose(self):
		self.segments = None