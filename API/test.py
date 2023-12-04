Airline_names = [
    'Air Arabia', 'Air Canada', 'Air China', 'Air France', 'Air India',
    'American Airlines', 'Austrian', 'British Airways', 'Brusseis',
    'Cathay Pacific', 'China Eastern', 'China Southern', 'Delta',
    'Easy Jet', 'Emirates', 'Etihad', 'IndiGo', 'Korean Air',
    'Lufthansa', 'Luxiar', 'Malaysia Airlines', 'Malindo Air',
    'Nepal Airlines', 'Qantas', 'Qatar Airways', 'SWISS',
    'Singapore Airlines', 'SriLankan Airlines', 'THAI',
    'Turkish Airlines', 'United Airlines', 'Virgin Atlantic',
    'Vueling', 'flydubai']


airline_dict = {}

for items in Airline_names:
    airline_dict[items.lower()] = 0

# print(Airline_dict)    


def parse_airline(x: str) -> dict:
    my_str = x.lower()
    for key, value in airline_dict.items():
        if key == my_str:
            airline_dict[key] = 1
    return airline_dict


(parse_airline("Turkish Airlines"))

airline_array = list(airline_dict.values())

# print(array)


# List of departure locations
Departure_locations = ['Beijing', 'Berlin', 'Chicago',
                       'Delhi', 'Dubai', 'Kathmandu', 'London', 'New Delhi', 'New York',
                       'Paris', 'Sydney']


departure_dict = {}

for items in Departure_locations:
    departure_dict[items.lower()] = 0

def parse_departure (x: str) -> dict:
    my_str = x.lower()
    for key, value in departure_dict.items():
            if key == my_str:
                departure_dict[key] = 1
    return departure_dict    

airline_array = list(airline_dict.values())


# List of destination locations
Destination_locations = ['Beijing', 'Berlin', 'Chicago', 'Dubai',
                          'Kathmandu', 'London', 'New Delhi',
                          'New York', 'Singapore', 'Sydney']


destination_dict = {}

for items in Departure_locations:
    destination_dict[items.lower()] = 0

def parse_destination (x: str) -> dict:
    my_str = x.lower()
    for key, value in destination_dict.items():
            if key == my_str:
                destination_dict[key] = 1
    return destination_dict
    

# List of flight class types
Flight_Class_type = ['Business', 'Economy', 'First']


flightclass_dict = {}

for items in Flight_Class_type:
    flightclass_dict[items.lower()] = 0

def parse_flightclass (x: str) -> dict:
    my_str = x.lower()
    for key, value in flightclass_dict.items():
            if key == my_str:
                flightclass_dict[key] = 1
    return flightclass_dict    