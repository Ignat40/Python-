from lzma import is_check_supported
from operator import is_


class Vehicle:
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation):
        self.id = listing_id
        self.price = price 
        self.max_speed = max_speed
        self.number_of_seats = number_of_seats
        self.year_of_creation = year_of_creation


    def print_vechicle_type(self):
        print("Base Vechicle")

    def listing_information(self) ->str:
        return str(self.id) + " " + str(self.price) + " " + str(self.max_speed) + " " + str(self.number_of_seats) + " " + str(self.year_of_creation) 
        
class Bicycle(Vehicle):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, brand, is_mountain):
        super(Bicycle, self).__init__(listing_id, price, max_speed, number_of_seats, year_of_creation)
        self.brand = brand
        self.is_mountain = is_mountain

    def print_vechicle_type(self):
       print ("Bicycle")

    def listing_information(self) -> str:
                return str(self.id) + " " + str(self.price) + " " + str(self.max_speed) + " " + str(self.number_of_seats) + " " + str(self.year_of_creation)+ " " + str(self.brand) + " " + str(self.is_mountain)  

class Engine:
    def __init__(self, fuel_type, engine_size):
        self.fuel_type = fuel_type
        self.engine_size = engine_size

class Motor_Vechicle(Vehicle, Engine):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight):
        Vehicle.__init__(listing_id, price, max_speed, number_of_seats, year_of_creation)
        Engine.__init__(self, fuel_type, engine_size)
        
        self.is_accident_free = is_accident_free
        self.weight = weight 

    def print_vechicle_type(self):
        print("Motor vechicle")

    def listing_information(self) -> str:
        return f"{self.listing_information} {self.price} {self.year_of_creation} {self.fuel_type} {self.engine_size} {self.is_accident_free} {self.weight} {self.max_speed} {self.year_of_creation}"


class Car(Motor_Vechicle):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight, brand, model, airbags, mileage):
        super(Car, self).__init__(listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight)

        self.brand = brand
        self.model = model 
        self.airbags = airbags
        self.mileage = mileage

    def print_vechicle_type(self):
        print("Car")

class Motorcycle(Motor_Vechicle):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight, brand, model, is_sport_bike, mileage):
        super(Motorcycle, self).__init__(listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight)
        self.brand = brand
        self.model = model
        self.is_sport_bike = is_sport_bike
        self.mileage = mileage

    def print_vechicle_type(self):
        print("Motorcycle")

class Boat(Motor_Vechicle):
    def __init__(self, listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight, brand, mileage):
        super(Boat, self).__init__(listing_id, price, max_speed, number_of_seats, year_of_creation, fuel_type, engine_size, is_accident_free, weight)
        
        self.brand = brand
        self.mileage = mileage

class Automobile_shop:
    items = []

    def list_vehicles(self):
        pass

    def add_vehicle(self, vehicle: Vehicle):
        pass

    def remove_vehicle(self, id_number: int):
        pass

    def sort_by_price(self):
        pass

