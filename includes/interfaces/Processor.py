import abc

class Processor(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def process(self):
		raise Exception('Compulsary implementation of process method. Process method will trigger process method of the subclasses')