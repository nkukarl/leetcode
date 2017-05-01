from unittest import TestCase

from mini_parser import Solution


class TestMiniParser(TestCase):
    def test_deserialize_int(self):
        # Setup
        sol = Solution()
        s = '324'

        # Exercise
        nested_integer = sol.deserialize(s)

        # Verify
        self.assertTrue(nested_integer.is_integer())
        self.assertEqual(nested_integer.get_integer(), 324)
        self.assertIsNone(nested_integer.get_list())

    def test_deserialize_list(self):
        # Setup
        sol = Solution()
        s = '[123, -123, [456, -456, [789, -789]]]'

        # Exercise
        nested_integer = sol.deserialize(s)

        # Verify
        self.assertFalse(nested_integer.is_integer())
        lst = nested_integer.get_list()
        self.assertEqual(lst[:2], [123, -123])
        lst_ = lst[-1].get_list()
        self.assertEqual(lst_[:2], [456, -456])
        lst__ = lst_[-1].get_list()
        self.assertEqual(lst__, [789, -789])
