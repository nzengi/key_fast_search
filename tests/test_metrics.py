import unittest
from fast_key_search.metrics import hamming_distance, euclidean_distance

class TestMetrics(unittest.TestCase):
    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(0b10101, 0b10000), 2)

    def test_euclidean_distance(self):
        self.assertEqual(euclidean_distance(10, 3), 7)

if __name__ == "__main__":
    unittest.main()
