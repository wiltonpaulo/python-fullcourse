class Game:
    def __init__(self, name, category, console, id=None):
        self.id = id
        self.name = name
        self.category = category
        self.console = console


class User:
    def __init__(self, name, nickname, password):
        self.name = name
        self.nickname = nickname
        self.password = password
