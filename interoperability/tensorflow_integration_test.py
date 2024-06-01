import unittest
import torch
import tensorflow as tf

class TestTensorFlowIntegration(unittest.TestCase):
    def test_integrate_with_tensorflow(self):
        torch_model = torch.nn.Sequential(
            torch.nn.Linear(10, 64),
            torch.nn.Linear(64, 10)
        )
        integration = TensorFlowIntegration(torch_model)
        integration.integrate_with_tensorflow()
        self.assertIsInstance(integration.model, tf.keras.Model)

if __name__ == "__main__":
    unittest.main()
