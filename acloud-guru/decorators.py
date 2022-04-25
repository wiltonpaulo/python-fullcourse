def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        return val

    return wrapped_func


@inspect
def combine(a, b):
    return a + b


class User:
    base_url = "https://example.com/api"

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + "?" + query_string

    @staticmethod
    def name():
        return "Kevin Bacon"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# User.name()
# User.query("name=test")
# user = User("Keith", "Thompson")
# print(user.baseurl)
# print(user.full_name)
