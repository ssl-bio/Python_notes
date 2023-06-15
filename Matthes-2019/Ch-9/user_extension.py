class Privilege():
    """Describes privileges of a user
    """
    default_powers = ["add post", "flag post", "edit post", "delete post"]

    def __init__(self, privileges=default_powers):
        # super(Privilege, self).__init__()
        self.privileges = privileges

    def show_privileges(self):
        print("As an Admin you can:")
        for power in self.privileges:
            print(f"- {power}")
        print("----------")


class Admin(User):
    """Defines privileges of a root user
    """

    def __init__(self, first_name,
                 last_name, location,
                 language):
        super(Admin, self).__init__(first_name, last_name, location, language)
        self.sudo_powers = Privilege()
