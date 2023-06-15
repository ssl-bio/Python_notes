class Employee():
    """Definies a default employee
    """

    def __init__(self, first_name, last_name, annu_salary):
        # super(Employee, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.annu_salary = annu_salary

    def give_raise(self, amount=5000):
        self.annu_salary += int(amount)
