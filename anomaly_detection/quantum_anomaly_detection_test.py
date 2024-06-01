# quantum_anomaly_detection_test.py

import unittest
import numpy as np
from quantum_anomaly_detection import run_quantum_anomaly_detection

class TestQuantumAnomalyDetection(unittest.TestCase):
    def test_quantum_anomaly_detection(self):
        # Create some dummy training and testing data
        training_data = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
        testing_data = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])

        # Create a quantum instance
        quantum_instance = qk.Aer.get_backend("qasm_simulator")

        # Run the quantum anomaly detection
        run_quantum_anomaly_detection(training_data, testing_data, quantum_instance)

        # Check if the accuracy is close to 1
        self.assertAlmostEqual(1, accuracy, places=2)

if __name__ == "__main__":
    unittest.main()
