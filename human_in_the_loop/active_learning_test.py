import unittest
import torch
from active_learning import uncertainty_sampling, query_by_committee, coreset_sampling

class TestActiveLearning(unittest.TestCase):
    def test_uncertainty_sampling(self):
        model = HumanInTheLoopModel(10, 5, 3)
        x = torch.randn(10, 10)
        y = torch.randint(0, 3, (10,))
        x_query, y_query = uncertainty_sampling(model, x, y, 2)
        self.assertIsInstance(x_query, torch.Tensor)
        self.assertIsInstance(y_query, torch.Tensor)

    def test_query_by_committee(self):
        models = [HumanInTheLoopModel(10, 5, 3) for _ in range(5)]
        x = torch.randn(10, 10)
        y = torch.randint(0, 3, (10,))
        x_query, y_query = query_by_committee(models, x, y, 2)
        self.assertIsInstance(x_query, torch.Tensor)
        self.assertIsInstance(y_query, torch.Tensor)

    def test_coreset_sampling(self):
        model = HumanInTheLoopModel(10, 5, 3)
        x = torch.randn(10, 10)
        y = torch.randint(0, 3, (10,))
        x_query, y_query = coreset_sampling(model, x, y, 2)
        self.assertIsInstance(x_query, torch.Tensor)
        self.assertIsInstance(y_query, torch.Tensor)

if __name__ == "__main__":
    unittest.main()
