import datetime
import unittest
from mltoolbox.datascrape import search_city


class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = weather.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)