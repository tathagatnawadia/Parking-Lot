print("Hello Gojek")

class Registration_number():
	delimiter = "-"
	def __init__(self, registration_number):
		self.segments = registration_number.split(Registration_number.delimiter)
		self.registration_number = registration_number


s = Registration_number("KA-23-22-33434")
print(s.segments)

