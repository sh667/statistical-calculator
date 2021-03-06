import unittest
from Statistics.RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random_generator = RandomGenerator()

    # Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
    def test_generate_rand_num_by_range_wo_seed(self):
        self.assertLessEqual(self.random_generator.generate_rand_num_by_range_wo_seed(3, 5), 5)
        self.assertGreaterEqual(self.random_generator.generate_rand_num_by_range_wo_seed(3, 5), 3)

    # Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
    def test_generate_rand_num_by_range_w_seed(self):
        self.assertLessEqual(self.random_generator.generate_rand_num_by_range_w_seed(5, 2, 3, 5), 5)
        self.assertGreaterEqual(self.random_generator.generate_rand_num_by_range_w_seed(5, 2, 3, 5), 3)

    # Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
    def test_get_rand_num_list_by_range_w_seed(self):
        data = self.random_generator.get_rand_num_list_by_range_w_seed(5, 2, 2, 1, 9)
        for num in range(len(data)):
            self.assertLessEqual(data[num], 9)
            self.assertGreaterEqual(data[num], 1)

    # Set a seed and randomly.select the same value from a list
    def test_set_seed_and_get_rand_from_list(self):
        self.assertEqual(self.random_generator.set_seed_and_get_rand_from_list(3, 2, [5, 3, 2, 1, 9]), 3)

    # Select a random item from a list
    def test_get_rand_item_from_list(self):
        self.assertTrue(self.random_generator.get_rand_item_from_list([5, 3, 2, 1, 9]) in [5, 3, 2, 1, 9])

    # Select N number of items from a list without a seed
    def test_get_rand_num_list_wo_seed(self):
        self.assertEqual(len(self.random_generator.get_rand_num_list_wo_seed(3, [5, 3, 2, 1, 9])), 3)
        self.assertTrue(set(self.random_generator.get_rand_num_list_wo_seed(3, [5, 3, 2, 1, 9])).issubset(set([5, 3, 2, 1, 9])))

    # Select N number of items from a list with a seed
    def test_get_rand_num_list_w_seed(self):
        self.assertEqual(len(self.random_generator.get_rand_num_list_w_seed(3, 2, 2, [5, 3, 2, 1, 9])), 3)
        self.assertTrue(set(self.random_generator.get_rand_num_list_w_seed(3, 2, 2, [5, 3, 2, 1, 9])).issubset(set([5, 3, 2, 1, 9])))


if __name__ == '__main__':
    unittest.main()
