from email import message


class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author

    def get_post_info(self):
        print(f"Post: {self.message} writter by {self.author}")
