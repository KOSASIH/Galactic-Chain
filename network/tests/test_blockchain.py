import unittest
from blockchain.blockchain import Blockchain
from blockchain.blockchain_storage import BlockchainStorage

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain_storage = BlockchainStorage()
        self.blockchain = Blockchain(self.blockchain_storage)

    def test_blockchain_init(self):
        self.assertEqual(self.blockchain.blocks, [])

    def test_add_block(self):
        block = Block(1, [], "0x0000000000000000000000000000000000000000000000000000000000000000")
        self.blockchain.add_block(block)
        self.assertEqual(self.blockchain.blocks, [block])

    def test_add_multiple_blocks(self):
        block1 = Block(1, [], "0x0000000000000000000000000000000000000000000000000000000000000000")
        block2 = Block(2, [], "0x0000000000000000000000000000000000000000000000000000000000000001")
        self.blockchain.add_block(block1)
        self.blockchain.add_block(block2)
        self.assertEqual(self.blockchain.blocks, [block1, block2])

    def test_get_latest_block(self):
        block1 = Block(1, [], "0x0000000000000000000000000000000000000000000000000000000000000000")
        block2 = Block(2, [], "0x0000000000000000000000000000000000000000000000000000000000000001")
        self.blockchain.add_block(block1)
        self.blockchain.add_block(block2)
        self.assertEqual(self.blockchain.get_latest_block(), block2)

if __name__ == "__main__":
    unittest.main()
