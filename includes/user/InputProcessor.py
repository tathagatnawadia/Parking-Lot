from includes.interfaces.Processor import Processor
from includes.configs.Defaults import Default

class InputProcessor(Processor):
	@staticmethod
	def process(processor, user_input):
		command, params = InputProcessor.parse_input(user_input)
		print(processor.process(command)(params))

	@staticmethod
	def parse_input(user_input):
		return user_input.split()[Default.COMMAND_INDEX], user_input.split()[Default.PARAM_INDEX:]