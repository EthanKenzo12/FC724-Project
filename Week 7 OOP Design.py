class Vehicle:
    """Vehicle class that controls common attributes of all vehicles.

    Attributes:
        None
    """

    # Note that the class docstring does not contain information about the methods in the class.
    # Each class method should contain its own docstring that describes the individual method.
    def move(distance):
        print(f"The car moved {distance} meters!")


class Car(Vehicle):
    """Car inehrits from Vehicle.

    Attributes:
        make: str | manufacturer of car object
        model: str | model number of car object
        year: str | release date of car object
        fuel_tank_capacity: float | capacity (in litres) of car object's fuel tank
        fuel_tank_level: float | current amount of fuel, initialized to be the tank's capacity.
    """

    def __init__(self, make, model, year, fuel_tank_capacity):
        """Inits the Car class.
        """
        self.make = make
        self.model = model
        self.year = year
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_level = fuel_tank_capacity

    def start(self):
        """Indicates the car has started.
        """
        print("Car has started.")

    def stop(self):
        """Indicates the car has stopped.
        """
        print("Car has stopped.")

    def honk(self):
        """Produces a loud honk.
        """
        print("Honk!")

    def refuel_message(self):
        """Conditional refuel message called inside Car.move()
        """
        if self.fuel_level <= self.fuel_tank_capacity / 10:
            print("You need to fill up!")

    def move(self, distance):
        """Extends Vehicle.move()

        Ammends fuel level depending on distance travelled, prints conditional message asking
        use to check fuel level.

        Args:
            distance: float | Distance in meters travelled by the car.

        Variables:
            fuel_usage: float | constant fuel usage defined based on distance,
                                in reality based on make and model of the car.
        """
        Vehicle.move(distance)
        fuel_usage = distance * 0.45
        self.fuel_level -= fuel_usage
        self.refuel_message()


class ElectricCar(Car):
    """Car inehrits from Vehicle.

    Attributes:
        make: str | manufacturer of car object
        model: str | model number of car object
        year: str | release date of car object
        battery_capacity: float | capacity (in kWh) of car object's battery
        battery_charge: float | current amount of charge, initialized to be the battery's capacity.
    """

    def __init__(self, make, model, year, battery_capacity):
        """Initiates the ElectricVehicle class.
        """
        # self.make = make
        # self.model = model
        # self.year = year
        super().__init__
        self.battery_capacity = battery_capacity
        self.battery_charge = battery_capacity

    def recharge(self):
        """Conditional recharge message called inside ElectricCar.move()
        """
        if ElectricCar.battery_charge <= ElectricCar.battery_capacity / 10:
            print("The battery needs to be recharged!")

    def move(self, distance):
        """Extends Vehicle.move()

        Ammends battery level depending on distance travelled, prints conditional message asking
        use to check battery level.

        Args:
            distance: float | Distance in meters travelled by the car.

        Variables:
            battery_usage: float | constant battery usage defined based on distance,
                                in reality based on make and model of the car.
        """
        Vehicle.move(distance)
        battery_usage = distance * 0.25
        Car.battery_level -= battery_usage


if __name__ == "__main__":
    my_car1 = Car(make="Mazda", model="MX-5", year="2005", fuel_tank_capacity=45)
    my_car2 = Car(make="Ford", model="KA", year="2010", fuel_tank_capacity=35)
    my_car3 = Car(make="Ferrari", model="Tipo 815", year="1940", fuel_tank_capacity=90)
    my_car4 = ElectricCar(make="Tesla", model="Model 3", year="2017", battery_capacity=57.5)

    print(my_car3.fuel_level)
    my_car3.move(100)
    print(my_car3.fuel_level)
    my_car3.move(100)

