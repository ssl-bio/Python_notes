import unittest
from city_functions import format_city


class FormatTestCase(unittest.TestCase):
    """Test the format of a city and its country

    """
    def test_city_country(self):
        iformat = format_city('la paz', 'bolivia')
        self.assertEqual(iformat, 'La Paz, Bolivia')

    def test_city_country_population(self):
        iformat = format_city('la paz', 'bolivia', 850_000)
        self.assertEqual(iformat, 'La Paz, Bolivia - 850000')


if __name__ == '__main__':
    unittest.main()
