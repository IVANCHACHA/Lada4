

import unittest
from rectangle import area, perimeter

class TestRectangle(unittest.TestCase):
    def test_area_positive(self):
        # Тест для проверки площади при положительных значениях
        self.assertEqual(area(5, 3), 15)
        self.assertEqual(area(10, 10), 100)

    def test_area_zero(self):
        # Тест для проверки площади при нулевых значениях
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_negative(self):
        # Тест для проверки площади при отрицательных значениях (должно вызывать ошибку)
        with self.assertRaises(ValueError):
            area(-5, 3)

    def test_perimeter_positive(self):
        # Тест для проверки периметра при положительных значениях
        self.assertEqual(perimeter(5, 3), 16)
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_zero(self):
        # Тест для проверки периметра при нулевых значениях
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_negative(self):
        # Тест для проверки периметра при отрицательных значениях (должно вызывать ошибку)
        with self.assertRaises(ValueError):
            perimeter(-5, 3)

if __name__ == "__main__":
    unittest.main()
