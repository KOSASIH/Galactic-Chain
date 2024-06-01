import unittest
from galactic_chain.anomaly_detection import AnomalyDetection

class TestAnomalyDetection(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})

    def test_one_class_svm(self):
        anomaly_detection = AnomalyDetection(self.data)
        ocsvm = anomaly_detection.one_class_svm()
        self.assertIsInstance(ocsvm, OneClassSVM)

if __name__ == '__main__':
    unittest.main()
