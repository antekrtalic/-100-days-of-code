import unittest
from city_functions import get_location

class LocationTestCase(unittest.TestCase):
    """Checking for correct string."""

    def test_city_country(self):
        """Does sentence like 'Rio De Janeiro, Brasil.' work?"""
        formatted_location = get_location('rio de janeiro', 'brasil')
        self.assertEqual(formatted_location, 'Rio De Janeiro, Brasil.')

    def test_city_country_population(self):
        """"Does sentence like 'Rio De Janeiro, Brasil, 5000000' work?"""
        formatted_location = get_location('rio de janeiro', 'brasil', 5000000)
        self.assertEqual(formatted_location, 'Rio De Janeiro, Brasil - Population 5000000')