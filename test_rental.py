import unittest

from rental_main import *


class Testrent(unittest.TestCase):
    def test_rent_start(self):
        itemz = {
            "6ft ladder": {
                "quantity": 1,
                "rent": 10,
                "value": 70
            },
            "12ft ladder": {
                "quantity": 2,
                "rent": 15,
                "value": 100
            },
            "drill": {
                "quantity": 4,
                "rent": 20,
                "value": 150
            }
        }

        new_q = rent_start(itemz, "6ft ladder")
        assert new_q == 0

    if __name__ == '__main__':
        unittest.main()
