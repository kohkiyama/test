import unittest
from ALU import total


class TestTotal(unittest.TestCase):

    def test_Total(self):
        val = total(1, 2)
        self.assertEqual(3, val)

    def test_Total_pp(self):
        val = total(2, 6)
        self.assertTrue(val > 0)

    def test_Total_nn(self):
        val = total(-2, -6)
        self.assertTrue(val < 0)


if __name__ == "__main__":
    unittest.main()
