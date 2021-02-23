import unittest
from employe import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create a survey for testing adding amount by default and by choice.
        """
        first = "What is your first name?"
        last = "What is your last name?"
        self.my_survey = Employee(first, last)
        self.salary = [5000, 2000, 8000]


    def test_give_default_raise(self):
        """Tests if default raise works."""
        self.my_survey.test_give_default_raise(self.salary[0])
        self.assertIn(self.salary[0], self.my_survey.salary)


    def test_give_custom_raise(self):
        """Tests if custom raise works"""

        for salari in self.salary:
            self.my_survey.test_give_custom_raise(salari)
        for salari in self.salary:
            self.assertIn(salari, self.my_survey.salary)



if __name__ == '__main__':
    unittest.main()