import unittest
from block.block import Block
from block.block_validator import BlockValidator

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block_validator = BlockValidator()
        self.block = Block(1, [], "0x0000000000000000000000000000000000000000000000000000000000000000")

    def test_block_init(self):
        self.assertEqual(self.block.block_id, 1)
        self.assertEqual(self.block.transactions, [])
        self.assertEqual(self.block.previous_hash, "0x0000000000000000000000000000000000000000000000000000000000000000")

    def test_block_validate(self):
        self.assertTrue(self.block_validator.validate(self.block))

    def test_block_invalid_transactions(self):
        self.block.transactions = ["invalid transaction"]
        self.assertFalse(self.block_validator.validate(self.block))

    def test_block_invalid_previous_hash(self):
        self.block.previous_hash = "invalid previous hash"
        self.assertFalse(self.block_validator.validate(self.block))

if __name__ == "__main__":
    unittest.main()
