import unittest
import torch
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from interoperability import Interoperability

class TestInteroperability(unittest.TestCase):
    def test_convert_to_torch(self):
        tf_model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, input_shape=(10,)),
            tf.keras.layers.Dense(10)
        ])
        interoperability = Interoperability(tf_model)
        torch_model = interoperability.convert_to_torch()
        self.assertIsInstance(torch_model, torch.nn.Module)

    def test_convert_to_tensorflow(self):
        torch_model = torch.nn.Sequential(
            torch.nn.Linear(10, 64),
            torch.nn.Linear(64, 10)
        )
        interoperability = Interoperability(torch_model)
        tf_model = interoperability.convert_to_tensorflow()
        self.assertIsInstance(tf_model, tf.keras.Model)

    def test_convert_to_sklearn(self):
        torch_model = torch.nn.Sequential(
            torch.nn.Linear(10, 64),
            torch.nn.Linear(64, 10)
        )
        interoperability = Interoperability(torch_model)
        sklearn_model = interoperability.convert_to_sklearn()
        self.assertIsInstance(sklearn_model, RandomForestClassifier)

if __name__ == "__main__":
    unittest.main()
