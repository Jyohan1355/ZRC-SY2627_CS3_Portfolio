from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_data(self):
        pass


class PHMeter(Sensor):

    def get_data(self):
        return "7.0 pH"


p = PHMeter()
print("Success!")