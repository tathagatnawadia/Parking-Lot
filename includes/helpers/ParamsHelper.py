from includes.configs.Defaults import Default, Action

class ParamsHelper(object):
	@staticmethod
	def getParams(action, params):
		if action == Action.PARK:
			return params[0], params[1]
		elif action == Action.LEAVE or action == Action.CREATE_PARKING_LOT:
			return int(params[0])
		elif action == Action.SEARCH_BY_COLOR or action == Action.SEARCH_BY_REGISTRATION:
			return params[0]
			