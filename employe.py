class Employee:
    """Definining method for user first, last name and annual salary."""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.salary = [0]

    """Defining method for adding salary."""

    def test_give_default_raise(self, default_add=5000):
        """Adds  default amount."""
        self.salary.append(default_add)


    def test_give_custom_raise(self, custom_add):
        """Adds custom amount."""
        custom_add = int(input("How much amount of money would you like to add? "))
        self.salary.append(custom_add)

