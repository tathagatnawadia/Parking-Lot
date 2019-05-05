import datetime
import sys

from includes.log.AppLogger import logging
from includes.configs.Defaults import Default
from includes.user.InputProcessor import InputProcessor

from includes.ParkingManager import ParkingManager

# We declare a singleton parking manager and pass the instance to the InputProcessor class to process user commands
myParking = ParkingManager()

# 2 modes of input - command line and interactive
if len(sys.argv) == 2:
	with open(sys.argv[1], "r") as input_file:
		for user_input in input_file:
			InputProcessor.process(myParking, user_input)
elif len(sys.argv) == 1:
	while True:
		user_input = input()
		if user_input == Default.EXIT_CODE or user_input == Default.EMPTY:
			break
		InputProcessor.process(myParking, user_input)
else:
	print("Correct Usage : ./main.py file_path_to_input.flat \n OR ")
	print("Correct Usage : ./main.py")
