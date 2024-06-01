import unittest
from galactic_chain.hyperparameter_tuning import HyperparameterTuning

class TestHyperparameterTuning(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})
        self.target = pd.Series([0, 0, 1, 1, 1])
        self.model = lambda x: x['A'] + x['B']

    def test_grid_search(self):
        hyperparameter_tuning = HyperparameterTuning(self.model, self.data, self.target)
        params = {'n_estimators': [10, 50, 100]}
        result = hyperparameter_tuning.grid_search(params)
        self.assertIn('n_estimators', result)

    def test_random_search(self):
        hyperparameter_tuning= HyperparameterTuning(self.model, self.data, self.target)
        params = {'n_estimators': [10, 50, 100]}
        result = hyperparameter_tuning.random_search(params, 5)
        self.assertIn('n_estimators', result)

if __name__ == '__main__':
    unittest.main()
