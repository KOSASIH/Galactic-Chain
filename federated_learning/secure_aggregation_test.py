import unittest
import torch
from federated_learning import load_model
from secure_aggregation import secure_aggregation

class TestSecureAggregation(unittest.TestCase):
    def test_secure_aggregation(self):
        models = [load_model() for _ in range(5)]
        aggregated_model = secure_aggregation(models)
        self.assertIsInstance(aggregated_model, dict)

if __name__ == "__main__":
    unittest.main()
