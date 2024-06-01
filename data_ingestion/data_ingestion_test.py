import unittest
from data_ingestion import ingest_data

class TestDataIngestion(unittest.TestCase):
    def test_ingest_data(self):
        data = {"sensor_id": 1, "temperature": 25.5, "timestamp": 1643723400}
        ingest_data(data)
        # Add assertions here to verify that the data was ingested correctly

if __name__ == "__main__":
    unittest.main()
