from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_data(self):
        pass


s = Sensor()
print("Success!")