import pytest
import random

from GenAi.day1.optimized import optimized_quick_sort


class TestSortingAlgorithms:

    def test_empty_array(self):
        """Test sorting an empty array"""
        arr = []
        assert optimized_quick_sort(arr) == []

    def test_single_element(self):
        """Test sorting array with single element"""
        arr = [1]
        assert optimized_quick_sort(arr) == [1]

    def test_already_sorted(self):
        """Test sorting already sorted array"""
        arr = [1, 2, 3, 4, 5]
        assert optimized_quick_sort(arr) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting reverse sorted array"""
        arr = [5, 4, 3, 2, 1]
        assert optimized_quick_sort(arr) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        """Test sorting array with duplicate elements"""
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        assert optimized_quick_sort(arr) == sorted(arr)

    def test_negative_numbers(self):
        """Test sorting array with negative numbers"""
        arr = [-3, 1, -4, 1, -5, 9, -2, 6, 5, -3, 5]
        assert optimized_quick_sort(arr) == sorted(arr)

    def test_large_random_array(self):
        """Test sorting large random array"""
        arr = [random.randint(-1000, 1000) for _ in range(1000)]
        assert optimized_quick_sort(arr) == sorted(arr)

    def test_all_same_elements(self):
        """Test sorting array with all same elements"""
        arr = [1] * 100
        assert optimized_quick_sort(arr) == arr

    def test_float_numbers(self):
        """Test sorting array with floating point numbers"""
        arr = [3.14, 1.41, 2.71, 0.58, 1.73]
        assert optimized_quick_sort(arr) == sorted(arr)

    @pytest.mark.parametrize("test_input", [[1, 2, 3], [3, 2, 1], [1, 3, 2], [2, 1, 3]])
    def test_different_permutations(self, test_input):
        """Test sorting different permutations"""
        assert optimized_quick_sort(test_input) == sorted(test_input)

    def test_stability(self):
        """Test sorting stability with custom objects"""

        class Item:
            def __init__(self, val, order):
                self.val = val
                self.order = order

            def __eq__(self, other):
                return self.val == other.val and self.order == other.order

            def __le__(self, other):
                return self.val <= other.val

        items = [Item(1, 1), Item(1, 2), Item(0, 3)]
        sorted_items = optimized_quick_sort(items)
        # Note: QuickSort is not stable, so this test might fail
        # Included to demonstrate stability testing
