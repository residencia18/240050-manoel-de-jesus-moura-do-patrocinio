# import the library
from inmetpy.stations import InmetStation
inmet = InmetStation()

# list all inmet stations available
stations = inmet.get_stations() # get details of all stations available
print("stations",stations)
