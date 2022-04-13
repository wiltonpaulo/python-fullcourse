# python alura-python/best-practices/hints.py
class Name:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def testa(self, name: str) -> int:
    self.name = name
    return int(self.age)


def testegain() -> str:
    return 'again'


myname = Name('wilton "paulo" da silva', 39)
print(myname.name)
