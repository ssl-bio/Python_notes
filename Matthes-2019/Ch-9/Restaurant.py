class Restaurant():
    """Displays basic information of a restaurant

    """
    def __init__(self, name, cuisine_type):
        # super(Restaurant, self).__init__()
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"'{self.name.title()}' information:")
        print(f"Cuisine: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"The restaurant '{self.name.title()}' is open")


class IceCreamStand(Restaurant):
    """Class to model a Ice cream dely

    """
    def __init__(self, name, cuisine_type, flavors=None):
        super(IceCreamStand, self).__init__(name, cuisine_type)
        self.name = name
        self.cuisine = cuisine_type
        self.flavors = flavors

    def show_flavors(self):
        if self.flavors:
            print(f"These are the available flavors at {self.name.title()}")
            for flavor in self.flavors:
                print(f"- {flavor.title()}")
        else:
            print("We don't have any ice creams, for now")

