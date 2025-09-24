class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self.vehicle_id = vehicle_id
        self.base_rate = base_rate

    def display_details(self):
        return f"ID: {self.vehicle_id}, Rate: ₹{self.base_rate}"

    def rental_charge(self):
        return 0.0 

class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self.base_rate * self.num_seats

class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self.base_rate * 0.5

def calculate_rental(vehicle):
    return vehicle.rental_charge()

car = Car("CAR001", 100, 4)
bike = Bike("BIKE001", 80, "Scooter")

print(car.display_details())
print("Car Charge:", calculate_rental(car))

print(bike.display_details())
print("Bike Charge:", calculate_rental(bike))
