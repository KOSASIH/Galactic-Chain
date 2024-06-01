import unittest
from blockchain import Blockchain
from data_provenance import DataProvenance

class TestDataProvenance(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
        self.data_provenance = DataProvenance(self.blockchain)

    def test_add_data(self):
        data = "Hello, world!"
        new_block = self.data_provenance.add_data(data)
        self.assertIsNotNone(new_block)
        self.assertEqual(new_block["data"], hashlib.sha256(data.encode()).hexdigest())

    def test_get_data_provenance(self):
        data = "Hello, world!"
        self.data_provenance.add_data(data)
        data_hash = hashlib.sha256(data.encode()).hexdigest()
        provenance = self.data_provenance.get_data_provenance(data_hash)
        self.assertIsNotNone(provenance)
        self.assertEqual(provenance["data"], data_hash)

if __name__ == "__main__":
    unittest.main()
