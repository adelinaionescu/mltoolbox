import datetime
import unittest
import datascrape


class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = weather.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)