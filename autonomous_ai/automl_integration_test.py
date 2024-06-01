# automl_integration_test.py

import unittest
import numpy as np
from automl_integration import automl_integration

class TestAutoMLIntegration(unittest.TestCase):
    def test_automl_integration(self):
        # Create some dummy data and target
        data = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
        target = np.array([0, 1, 1, 0])

        # Run the AutoML integration
        automl_model = automl_integration(data, target, "classification")

        # Check if the model can make predictions
        predictions = automl_model.predict(data)

        self.assertEqual(len(predictions), len(target))

if __name__ == "__main__":
    unittest.main()
