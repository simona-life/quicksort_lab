import unittest
from quick_sort import quicksort


class TestQuicksort(unittest.TestCase):
    input_array = [0, 5, -15, -3, 18, 1, -30]
    asc_array = [-30, -15, -3, 0, 1, 5, 18]
    desc_array = [18, 5, 1, 0, -3, -15, -30]

    def test_asc_sort(self):
        self.assertEqual(quicksort(self.input_array, 'asc', ), self.asc_array)

    def test_desc_sort(self):
        self.assertEqual(quicksort(self.input_array, 'desc'), self.desc_array)

    def test_asc_sort_of_desc_array(self):
        self.assertEqual(quicksort(self.desc_array, 'asc'), self.asc_array)

    def test_desc_sort_of_desc_array(self):
        self.assertEqual(quicksort(self.asc_array, 'desc'), self.desc_array)


if __name__ == '__main__':
    unittest.main()
