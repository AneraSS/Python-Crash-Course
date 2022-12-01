import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions."""
    def test_city_country(self):
        """Does 'Santiago, Chile' pairs work? """
        formatted_city_country = city_country('Santiago', 'Chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do 'Santiago, Chile - population: 5000000' pairs work?"""
        formatted_city_country = city_country('Santiago', 'Chile', population=5000000)
        self.assertEqual(formatted_city_country, 'Santiago, Chile - population: 5000000')

if __name__=='__main__':
    unittest.main()