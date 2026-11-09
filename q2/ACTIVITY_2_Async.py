
class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()


# Create objects
car = Car()
boat = Boat()
drone = Drone()

# Call start_trip() for each object
start_trip(car)
start_trip(boat)
start_trip(drone)
