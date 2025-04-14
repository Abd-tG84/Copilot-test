import unittest

class TestAddNumbers(unittest.TestCase):
    def test_add_integers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add_numbers(2.5, 3.5), 6.0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            add_numbers("a", 3)

if __name__ == "__main__":
    unittest.main()
