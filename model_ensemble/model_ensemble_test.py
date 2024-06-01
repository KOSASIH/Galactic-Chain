import unittest
from galactic_chain.model_ensemble import ModelEnsemble

class TestModelEnsemble(unittest.TestCase):
    def setUp(self):
        self.model1 = lambda x: x['A'] + x['B']
        self.model2 = lambda x: x['A'] - x['B']
        self.models = [self.model1, self.model2]

    def test_bagging(self):
        model_ensemble = ModelEnsemble(self.models)
        ensemble = model_ensemble.bagging()
        self.assertIsInstance(ensemble, BaggingClassifier)

if __name__ == '__main__':
    unittest.main()
