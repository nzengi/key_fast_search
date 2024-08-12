import unittest
from fast_key_search.search import Worker, collaborative_search

class TestSearch(unittest.TestCase):
    def test_worker_search(self):
        target = 0x1a838b13505b26867
        worker = Worker(0, 2**256 - 1, target)
        result = worker.search()
        self.assertEqual(result, target)

    def test_collaborative_search(self):
        target = 0x1a838b13505b26867
        worker1 = Worker(0, 2**255, target)
        worker2 = Worker(2**255 + 1, 2**256 - 1, target)
        result = collaborative_search([worker1, worker2])
        self.assertEqual(result, target)

if __name__ == "__main__":
    unittest.main()
