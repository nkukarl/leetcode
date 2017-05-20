from unittest import TestCase

from find_median_from_data_stream import MedianFinder


class TestFindMedianFromDataStream(TestCase):
    def test_median_finder(self):
        # Setup
        median_finder = MedianFinder()

        # Exercise and Verify
        median_finder.add_num(1)
        median_finder.add_num(2)
        self.assertEqual(median_finder.find_median(), 1.5)
        median_finder.add_num(3)
        self.assertEqual(median_finder.find_median(), 2)
