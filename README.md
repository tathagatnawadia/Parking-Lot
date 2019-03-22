### TODODODO

* Item Multilayered car parking - done
* Item Duplicate car parking - done
* Item Maybe the guy lost the ticket and just remembers the car number and color - dunno
* Item Lock a vechile and prevent allocation/deallocation - have to add
* Item Deallocating an already deallocated - done
* Item Maybe a vechile requires more than 1 parking slot - dunno
* Item Maybe have 2 or more colors to match - done
* Item Synchronise multiple parking lot data - dunno
* Item Auditor of data in a log file - done
* Item The test files are getting bloated - gotta add some fixtures and common functions
* Item Taking care of mutiple threads of the application - done
* Item bulk checkin/checkout - dunno

### Assumptions
* Item Colors and command are case sensitive (exactly as per the problem), not plannging to handle right now

### Structure
* Item main creates an instance of ParkingManager which can have multiple ParkingLot 
* Item ParkingManager takes care of all the ParkingLot in the tech park maybe
* Item ParkingLot is the interface between the ParkingManager and the ParkingRow
* Item ParkingRow stores all the registration and stuff

```console
includes
├── ParkingManager.py
├── configs
│   ├── Defaults.py
│   ├── Messages.py
│   └── UserCommands.py
├── entities
│   ├── ParkingRow.py
│   ├── Registration.py
│   └── Vechile.py
├── exceptions
│   └── AppExceptions.py
├── helpers
│   └── ParamsHelper.py
├── interfaces
│   ├── Dumper.py
│   └── Processor.py
├── log
│   └── AppLogger.py
├── usecases
│   ├── AdvertisementBoards.py
│   ├── CommunityHall.py
│   ├── ParkingLot.py
│   └── Shops.py
└── user
    └── InputProcessor.py
    
apptests
├── InputProcessorTest.py
├── ParkingLotTest.py
├── ParkingManagerTest.py
├── ParkingRowTest.py
└── RegistrationTest.py

bin
├── README.md
├── parking_lot
├── run_functional_tests
└── setup

parking_log
├── ParkingLot-1.4.2.pdf
├── README.md
├── Tathagat's\ Resume.pdf
├── main.py
└── tests.py
```
### Setup
```bash
$./bin/setup
```
### Performance & Memory Profiling 
```bash
$python3 -m cProfile main.py ./functional_spec/fixtures/file_input.txt
```
### Unittest 
```bash
$python3 -m unittest tests.py
$./bin/run_functional_tests
```
### Run the application
```bash
$python main.py ./functional_spec/fixtures/file_input.txt #(filebased)
$python main.py #(interactive)
$./bin/parking_lot ./functional_spec/fixtures/file_input.txt #(filebased)
$./bin/parking_lot #(interactive)
```

###### Note - just check if you are in sudo mode or enough permissions for ./bin/setup