#!/usr/bin/env python3

"""Unit test class.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from temp_convertk import convert_f2c, convert_c2f

class TestTemperatureConversion(unittest.TestCase):

    """Unit test class.
    """

    def test_fahrenheit_to_celsius(self):
        """Test conversion from Fahrenheit to Celsius.
        """
        self.assertAlmostEqual(convert_f2c(32), 0.0, places=2)
        self.assertAlmostEqual(convert_f2c(212), 100.0, places=2)
        self.assertAlmostEqual(convert_f2c(98.6), 37.0, places=1)

    def test_celsius_to_fahrenheit(self):
        """Test conversion from Celsius to Fahrenheit.
        """
        self.assertAlmostEqual(convert_c2f(0), 32.0, places=2)
        self.assertAlmostEqual(convert_c2f(100), 212.0, places=2)
        self.assertAlmostEqual(convert_c2f(37), 98.6, places=1)

    def test_invalid_input(self):
        """Test handling of invalid input (e.g., non-numeric input)
        """
        with self.assertRaises(TypeError):
            convert_f2c("abc")
        with self.assertRaises(TypeError):
            convert_c2f("def")

if __name__ == '__main__':
    unittest.main()
