from abc import ABC, abstractmethod


class Aircraft(ABC):

    @abstractmethod
    def __init__(self, speed):
        self.__speed = speed

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        print("All checks completed")

    @property
    @abstractmethod
    def speed(self):
        pass

    @speed.setter
    @abstractmethod
    def speed(self, value):
        pass


class Jet(Aircraft):
    def __init__(self, speed):
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()
        print("My jet has landed")


jet1 = Jet(900)
jet1.land()
print(jet1.speed)
jet1.speed = 950
print(jet1.speed)
