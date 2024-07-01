class Vehicle():

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def detail(self):
        print(f"I'm {self.name} {self.model}")

    def moves(self):
        print("moves along..")


my_car = Vehicle("Tesla", "T100")
my_car.detail()
my_car.moves()

your_car = Vehicle("Volvo", "V200")
your_car.detail()
your_car.moves()

print("\n\n")


class Bike(Vehicle):
    def __init__(self, name, model, cc):
        # self.name = name
        # self.model = model
        super().__init__(name, model)
        self.cc = cc

    def detail(self):
        print(f"I'm {self.name} {self.model} of {self.cc} CC")

    def moves(self):
        print("rides along..")


my_bike = Bike("TVS", "NTorq", 125)
my_bike.detail()
my_bike.moves()

print("\n\n")


class Jeep(Vehicle):
    def __init__(self, name, model, max_passenger):
        super().__init__(name, model)
        self.max_passenger = max_passenger

    def moves(self):
        print("rumbles along..")

    def detail(self):
        print(f"I'm {self.name} {self.model} with {self.max_passenger} seats")


my_jeep = Jeep("TATA", "SUMO", "8")
my_jeep.detail()
my_jeep.moves()

print("\n\n")


class Car(Vehicle):
    pass


fiat = Car("Fiat", "F456")
fiat.detail()
fiat.moves()

print("\n")
#####################################

for vehicle in (my_car, your_car, my_bike, my_jeep, fiat):
    vehicle.detail()
    vehicle.moves()
