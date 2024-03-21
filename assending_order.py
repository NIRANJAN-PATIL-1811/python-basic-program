import unittest

def is_sorted_ascending(arr):
    """
    Checks if a list is sorted in ascending order.
    Returns True if sorted, False otherwise.
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

class TestIsSortedAscending(unittest.TestCase):

    def test_sorted_list(self):
        self.assertTrue(is_sorted_ascending([1, 2, 3, 4, 5]))

    def test_unsorted_list(self):
        self.assertFalse(is_sorted_ascending([5, 4, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(is_sorted_ascending([]))

    def test_single_element_list(self):
        self.assertTrue(is_sorted_ascending([42]))

    def test_sorted_list_with_duplicates(self):
        self.assertTrue(is_sorted_ascending([1, 2, 2, 3, 4]))

    def test_unsorted_list_with_duplicates(self):
        self.assertFalse(is_sorted_ascending([1, 3, 2, 4, 3]))

if __name__ == '__main__':
    unittest.main()
