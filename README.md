###TODODODO

#### Multilayered car parking - done
#### Duplicate car parking - done
#### Maybe the guy lost the ticket and just remembers the car number and color - dunno
#### Lock a vechile and prevent allocation/deallocation - have to add
#### Deallocating an already deallocated - done
#### Maybe a vechile requires more than 1 parking slot - dunno
#### Maybe have 2 or more colors to match - done
#### Synchronise multiple parking lot data - dunno
#### Auditor of data in a log file - done
#### The test files are getting bloated - gotta add some fixtures and common functions
#### Taking care of mutiple threads of the application - done
#### bulk checkin/checkout - dunno

### Assumptions
#### Colors and command are case sensitive (exactly as per the problem), not plannging to handle right now

### Performance & Memory Profiling 
#### python -m cProfile main.py ./functional_spec/fixtures/file_input.txt

### Unittest 
#### python3 -m unittest tests.py
#### ./bin/run_functional_tests

### Run the application
#### (filebased) python main.py ./functional_spec/fixtures/file_input.txt
#### (interactive) python main.py
#### (filebased) ./bin/parking_lot ./functional_spec/fixtures/file_input.txt
#### (interactive) ./bin/parking_lot

