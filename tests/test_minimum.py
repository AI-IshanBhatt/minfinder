import unittest

from minfinder.minfinder import minimum


class TestMinimum(unittest.TestCase):

    def test_empty_array(self):
        with self.assertRaisesRegex(ValueError, "Empty"):
            minimum([])

    def test_one_element_array(self):
        arr = [2]
        self.assertEqual(2, minimum(arr))

    def test_two_elements_array(self):
        arr = [5, 7]
        self.assertEqual(5, minimum(arr))

    def test_right_skewed_array(self):
        arr = [100, 90, 80, 50, 55, 59, 75, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]
        self.assertEqual(50, minimum(arr))

    def test_left_skewed_array(self):
        arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 70, 60, 50, 55]
        self.assertEqual(50, minimum(arr))

    def test_character_array(self):
        c_arr = ["z", "y", "x", "w", "o", "a", "b", "c", "v"]
        self.assertEqual("a", minimum(c_arr))

    def test_string_array(self):
        str_arr = ["zz", "yy", "xx", "ff", "gg", "hh"]
        self.assertEqual("ff", minimum(str_arr))

    def test_float_array(self):
        float_arr = [-1.1, -2.2, -3.3, -4.4, 0.1, 1.1, 2.2]
        self.assertEqual(-4.4, minimum(float_arr))

    def test_int_float_array(self):
        mix_arr = [2.9, 3.7, 9.3, 15, 20]
        self.assertEqual(2.9, minimum(mix_arr))

    def test_custom_class_with_lt(self):
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def __lt__(self, other):
                return self.age < other.age

            def __str__(self):
                return f"{self.name}"

        persons = [Person("Ba", 90), Person("MP", 70), Person("MK", 60), Person("MB", 50),
                   Person("IS", 30), Person("GU", 29), Person("YA", 2), Person("MO", 65)]
        self.assertEqual("YA", str(minimum(persons)))

    def test_custom_class_wo_lt(self):
        class Vehicle:
            def __init__(self, make):
                self.make = make

        vehicles = [Vehicle("Toyota"), Vehicle("HYU"), Vehicle("MERC"), Vehicle("FER")]
        with self.assertRaisesRegex(TypeError, "'<' not supported"):
            minimum(vehicles)


