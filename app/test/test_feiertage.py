import unittest
from datetime import datetime

from feiertage import Neujahr_F, HeiligeDreiKoenige_F, Feiertag, calc_ostern, get_feiertage_as_list


class HolidayTestCase(unittest.TestCase):

    # Verify that correct dates are returned
    def test_feiertag_dates(self):
        feiertag = Neujahr_F()
        # in 2023, New year will fall on January 1, you can modify the year for checking in other years
        self.assertEqual(feiertag.date(2023), datetime(2023, 1, 1))

    # Verify functionality of 'is_for_me' method
    def test_is_for_me(self):
        feiertag = HeiligeDreiKoenige_F()
        self.assertEqual(feiertag.is_for_me('Baden-Württemberg'), True)
        self.assertEqual(feiertag.is_for_me('Hamburg'), False)


# Verify correct calculation of easter
class CalcOsternTestCase(unittest.TestCase):

    # verify calculation with known easter dates
    def test_calc_ostern(self):
        # Easter Sunday in year 2023 is April 9, you can modify the year for checking in other years
        self.assertEqual(calc_ostern(2023), datetime(2023, 4, 9))


# Verify output of 'get_feiertage_as_list' function
class GetFeiertageTestCase(unittest.TestCase):

    def test_get_feiertage_as_list(self):
        feiertage = get_feiertage_as_list()
        # Verify list is correct length
        self.assertEqual(len(feiertage), 19)
        # Verify list contains a specific Feiertag
        self.assertIsInstance(feiertage[0], Neujahr_F)


if __name__ == '__main__':
    unittest.main()
