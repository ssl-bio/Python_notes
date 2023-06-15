class User():
    """Displays information for a user
    """
    def __init__(self, first_name, last_name, location, language):
        # super(User, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.language = language

    def describe_user(self):
        user_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Name: {user_name}")
        print(f"Location: {self.location.title()}")
        print(f"Language: {self.language.title()}")

    def greet_user(self):
        iname = self.first_name.title()
        print(f"Welcome {iname}")
