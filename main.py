import datetime
import sys

from includes.log.AppLogger import Audit
from includes.configs.Defaults import Default
from includes.user.InputProcessor import InputProcessor

from includes.ParkingManager import ParkingManager

goJekParking = ParkingManager()

if len(sys.argv) == 2:
	input_file = open(sys.argv[1], "r")
	for user_input in input_file:
		InputProcessor.process(goJekParking, user_input)
elif len(sys.argv) == 1:
	while True:
		user_input = input()
		if user_input == Default.EXIT_CODE or user_input == Default.EMPTY:
			break
		else:
			InputProcessor.process(goJekParking, user_input)
else:
	print("Correct Usage : ./parking_lot.py file_path_to_input.flat \n OR ")
	print("Correct Usage : ./parking_lot.py")
