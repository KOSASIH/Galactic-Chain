import unittest
from blockchain import app, Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.blockchain = Blockchain()

    def test_create_block(self):
        block = self.blockchain.create_block(1, "0")
        self.assertIsNotNone(block)
        self.assertEqual(block["index"], 1)
        self.assertEqual(block["previous_hash"], "0")

    def test_calculate_hash(self):
        block = {"index": 1, "timestamp": 1643723400, "data": "", "previous_hash": "0", "hash": ""}
        hash = self.blockchain.calculate_hash(block)
        self.assertIsNotNone(hash)
        self.assertEqual(len(hash), 64)

    def test_is_valid_chain(self):
        chain = [{"index": 1, "timestamp": 1643723400, "data": "", "previous_hash": "0", "hash": "hash1"},
                 {"index": 2, "timestamp": 1643723401, "data": "", "previous_hash": "hash1", "hash": "hash2"}]
        self.assertTrue(self.blockchain.is_valid_chain(chain))

    def test_replace_chain(self):
        chain = [{"index": 1, "timestamp": 1643723400, "data": "", "previous_hash": "0", "hash": "hash1"},
                 {"index": 2, "timestamp": 1643723401, "data": "", "previous_hash": "hash1", "hash": "hash2"}]
        self.blockchain.replace_chain(chain)
        self.assertEqual(self.blockchain.chain, chain)

if __name__ == "__main__":
    unittest.main()
