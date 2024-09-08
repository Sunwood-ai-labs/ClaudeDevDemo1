import unittest
from circle_area import calculate_circle_area

class TestCircleArea(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(calculate_circle_area(1), 3.141592653589793, places=10)
        self.assertAlmostEqual(calculate_circle_area(0), 0)
        self.assertAlmostEqual(calculate_circle_area(2.5), 19.634954084936208, places=10)

if __name__ == "__main__":
    unittest.main()
