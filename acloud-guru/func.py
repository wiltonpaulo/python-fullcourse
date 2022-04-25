class Car:
    """
    Docstring describing the class
    """

    def __init__(self, car_name) -> None:
        self.car_name = car_name

    def __str__(self) -> str:
        return f"Soh uma string mano {self.car_name}"

    def anda(self):
        return f"Anda {self.car_name}"


car = Car("ecosport")
print(car.anda())
print(car)
