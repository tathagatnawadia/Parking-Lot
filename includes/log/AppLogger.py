import logging
from includes.configs.Defaults import Default
logging.basicConfig(filename=Default.LOG_FILENAME, filemode='w', 
	format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)