import abc

class Dumper(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def dump(self):
		raise Exception('Compulsary implementation of dump method which dumps all data in the object')