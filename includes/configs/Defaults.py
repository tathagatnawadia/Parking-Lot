class Default(object):
	VECHILE_TYPE = "CAR",
	ADMIN = "gojek"
	TIMING = None
	OWNER = "Prestige Group"
	COMMA_SEPERATOR = ", "
	REGISTRATION_DELIMITER = "-"
	NEWLINE = "\n"
	PARKING_SLOT_CODE = 0 #Assuming we may have multilevel and multiple parking slots
	EXIT_CODE = "exit"
	EMPTY = ""
	COMMAND_INDEX = 0
	PARAM_INDEX = 1
	LOG_FILENAME = "app.log"


class Action(object):
	PARK = 'park',
	LEAVE = 'leave',
	STATUS = 'status',
	SEARCH_BY_COLOR = 'search_by_color',
	SEARCH_BY_REGISTRATION = 'search_by_registration'
	CREATE_PARKING_LOT = 'create_parking_lot'