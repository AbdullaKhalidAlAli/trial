# -*- coding: utf-8 -*-
"""untitled65.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/NDM777777/dbe08e8e9df9f3c151509827dfa51633/untitled65.ipynb
"""

class Passenger:
    def __init__(self, passenger_id, first_name, last_name, date_of_birth, email):
        self._passenger_id = passenger_id
        self._first_name = first_name
        self._last_name = last_name
        self._date_of_birth = date_of_birth
        self._email = email

    # Setter and Getter methods for Passenger ID
    def set_passenger_id(self, passenger_id):
        self._passenger_id = passenger_id

    def get_passenger_id(self):
        return self._passenger_id

    # Setter and Getter methods for First Name
    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name

    # Setter and Getter methods for Last Name
    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    # Setter and Getter methods for Date of Birth
    def set_date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def get_date_of_birth(self):
        return self._date_of_birth

    # Setter and Getter methods for Email
    def set_email(self, email):
        self._email = email

    def get_email(self):
        return self._email

    # Placeholder function for additional functionality (e.g., update passenger details)
    def update_details(self):
        pass

    # Method to get the full name of the passenger
    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"


class BoardingPass:
    def __init__(self, boarding_pass_id, passenger_name, from_location, to_location, flight_number):
        self._boarding_pass_id = boarding_pass_id
        self._passenger_name = passenger_name
        self._from_location = from_location
        self._to_location = to_location
        self._flight_number = flight_number

    # Setter and Getter methods for Boarding Pass ID
    def set_boarding_pass_id(self, boarding_pass_id):
        self._boarding_pass_id = boarding_pass_id

    def get_boarding_pass_id(self):
        return self._boarding_pass_id

    # Setter and Getter methods for Passenger Name
    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def get_passenger_name(self):
        return self._passenger_name

    # Setter and Getter methods for From Location
    def set_from_location(self, from_location):
        self._from_location = from_location

    def get_from_location(self):
        return self._from_location

    # Setter and Getter methods for To Location
    def set_to_location(self, to_location):
        self._to_location = to_location

    def get_to_location(self):
        return self._to_location

    # Setter and Getter methods for Flight Number
    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def get_flight_number(self):
        return self._flight_number

    # Placeholder function for additional functionality (e.g., update boarding pass details)
    def update_details(self):
        pass

    # Method to display boarding pass details
    def display_boarding_pass_details(self):
        print("NATIONAL AIRLINES")
        print("PASSENGER TICKET AND BAGGAGE CHECK")
        print("\nBOARDING PASS")
        print("FIRST CLASS\n")
        print("Passenger")
        print(self._passenger_name)
        print("From:")
        print(self._from_location)
        print("\nFlight")
        print(self._flight_number)


class Flight:
    def __init__(self, flight_number, departure_city, destination_city, departure_time, arrival_time):
        self._flight_number = flight_number
        self._departure_city = departure_city
        self._destination_city = destination_city
        self._departure_time = departure_time
        self._arrival_time = arrival_time

    # Setter and Getter methods for Flight Number
    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def get_flight_number(self):
        return self._flight_number

    # Setter and Getter methods for Departure City
    def set_departure_city(self, departure_city):
        self._departure_city = departure_city

    def get_departure_city(self):
        return self._departure_city

    # Setter and Getter methods for Destination City
    def set_destination_city(self, destination_city):
        self._destination_city = destination_city

    def get_destination_city(self):
        return self._destination_city

    # Setter and Getter methods for Departure Time
    def set_departure_time(self, departure_time):
        self._departure_time = departure_time

    def get_departure_time(self):
        return self._departure_time

    # Setter and Getter methods for Arrival Time
    def set_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time

    def get_arrival_time(self):
        return self._arrival_time

    # Placeholder function for additional functionality (e.g., calculate flight duration)
    def calculate_flight_duration(self):
        pass


class BoardingPassSystem:
    def __init__(self, name, version, description, max_passenger_capacity, airport_code):
        self._name = name
        self._version = version
        self._description = description
        self._max_passenger_capacity = max_passenger_capacity
        self._current_passenger_count = 0  # Initial count is 0
        self._airport_code = airport_code

    # Setter and Getter methods for Name
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    # Setter and Getter methods for Version
    def set_version(self, version):
        self._version = version

    def get_version(self):
        return self._version

    # Setter and Getter methods for Description
    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    # Setter and Getter methods for Max Passenger Capacity
    def set_max_passenger_capacity(self, max_passenger_capacity):
        self._max_passenger_capacity = max_passenger_capacity

    def get_max_passenger_capacity(self):
        return self._max_passenger_capacity

    # Setter and Getter methods for Current Passenger Count
    def set_current_passenger_count(self, current_passenger_count):
        self._current_passenger_count = current_passenger_count

    def get_current_passenger_count(self):
        return self._current_passenger_count

    # Setter and Getter methods for Airport Code
    def set_airport_code(self, airport_code):
        self._airport_code = airport_code

    def get_airport_code(self):
        return self._airport_code

    # Placeholder function for additional functionality (e.g., generate boarding pass statistics)
    def generate_statistics(self):
        pass


# Create Passenger object
passenger = Passenger("1", "JAMES", "SMITH", "1980-01-01", "james.smith@example.com")

# Create BoardingPass object
boarding_pass = BoardingPass("1", passenger.get_full_name(), "CHICAGO ORD", "NEW YORK JFK", "NA4321")

# Create Flight object
flight = Flight("NA4321", "CHICAGO ORD", "NEW YORK JFK", "11:40", "13:30")

# Display boarding pass details
boarding_pass.display_boarding_pass_details()

# Display additional details for the Flight
print("\nAdditional Flight Details:")
flight_details = {
    "Gate": "03",
    "Date": "06 DEC 20",
    "Time": "11:40",
    "Boarding till": "11:20",
    "Seat": "09A",
    "Electronic ticket": "629",
    "Arrival time": "13:30",
    "Therminal": "2"
}
for key, value in flight_details.items():
    print(f"{key}\n{value}\n")