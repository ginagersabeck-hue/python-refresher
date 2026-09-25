import math
import random
import unittest
import my_utils


class TestMyUtils(unittest.TestCase):
    # positive test case with randomness#
    def test_get_mean_positive_random(self):
        # test get_mean with randomly genterated intergers
        rand_array = [random.randint(1, 100) for _ in range(50)]
        expected_mean = sum(rand_array)/len(rand_array)

        self.assertEqual(my_utils.get_mean(rand_array), expected_mean)

    def test_get_mean_positive_fixed(self):
        # test get_mean with a known fixed list of numbers
        test_array = [10, 20, 30, 40]
        self.assertEqual(my_utils.get_mean(test_array), 25.0)

    def test_get_median_odd_length(self):
        """Test get_median with an odd number of unsorted elements."""
        test_array = [9, 1, 5]
        # Sorted array is [1, 5, 9], so median is 5
        self.assertEqual(my_utils.get_median(test_array), 5)

    def test_get_median_even_length(self):
        """Test get_median with an even number of elements."""
        test_array = [10, 20, 30, 40]
        # Median is average of 20 and 30 -> 25.0
        self.assertEqual(my_utils.get_median(test_array), 25.0)

    def test_get_median_random(self):
        """Test get_median with a random sorted array."""
        rand_array = [random.randint(1, 500) for _ in range(11)]
        sorted_array = sorted(rand_array)
        expected_median = sorted_array[5]

        self.assertEqual(my_utils.get_median(rand_array), expected_median)

    def test_get_std_dev_positive(self):
        """Test get_std_dev with a known array."""
        test_array = [2, 4, 4, 4, 5, 5, 7, 9]
        # Mean = 5, Variance = 4, Std Dev = sqrt(4) = 2.0
        self.assertAlmostEqual(my_utils.get_std_dev(test_array), 2.0)

    def test_get_std_dev_zero_variance(self):
        """Test get_std_dev where all numbers are identical"""
        test_array = [7, 7, 7, 7]
        self.assertEqual(my_utils.get_std_dev(test_array), 0.0)

    # ==========================================
    # NEGATIVE TEST CASES (ERROR HANDLING)
    # ==========================================

    def test_get_mean_empty_list(self):
        """Test that get_mean raises ValueError when passed an empty list."""
        self.assertRaises(ValueError, my_utils.get_mean, [])

    def test_get_mean_none_input(self):
        """Test that get_mean raises TypeError when passed None."""
        self.assertRaises(TypeError, my_utils.get_mean, None)

    def test_get_median_empty_list(self):
        """Test that get_median raises ValueError when passed an empty list."""
        self.assertRaises(ValueError, my_utils.get_median, [])

    def test_get_median_none_input(self):
        """Test that get_median raises TypeError when passed None."""
        self.assertRaises(TypeError, my_utils.get_median, None)

    def test_get_std_dev_empty_list(self):
        """Test that get_std_dev raises ValueError w empty list."""
        self.assertRaises(ValueError, my_utils.get_std_dev, [])

    def test_get_std_dev_none_input(self):
        """Test that get_std_dev raises TypeError when passed None."""
        self.assertRaises(TypeError, my_utils.get_std_dev, None)


if __name__ == '__main__':
    unittest.main()
