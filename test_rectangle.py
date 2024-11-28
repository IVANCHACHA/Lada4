

import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(10, 10), 100)

    def test_area_zero(self):

        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)



    def test_perimeter_positive(self):

        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_zero(self):

        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_zero(self):

        self.assertEqual(perimeter(0, -5), 10)
        self.assertEqual(perimeter(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
