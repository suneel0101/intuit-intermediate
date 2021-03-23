import unittest


class TestLen(unittest.TestCase):

    def test_length_of_list(self):
        self.assertEqual(len([1, 3, 4, 1, 3]), 5, "Should be 5")

        
if __name__ == '__main__':
    unittest.main()