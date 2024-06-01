import unittest
from galactic_chain.explainability import Explainability

class TestExplainability(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})
        self.target = pd.Series([0, 0, 1, 1, 1])
        self.model = lambda x: x['A'] + x['B']

    def test_lime_explain(self):
        explainer = Explainability(self.model, self.data, self.target)
        instance = pd.Series({'A': 3, 'B': 4})
        explanation = explainer.lime_explain(instance)
        self.assertIsInstance(explanation, list)

    def test_shap_explain(self):
        explainer = Explainability(self.model, self.data, self.target)
        instance = pd.Series({'A': 3, 'B': 4})
        explanation = explainer.shap_explain(instance)
        self.assertIsInstance(explanation, np.ndarray)

    def test_tree_explain(self):
        explainer = Explainability(self.model, self.data, self.target)
        instance = pd.Series({'A': 3, 'B': 4})
        explanation = explainer.tree_explain(instance)
        self.assertIsInstance(explanation, dict)

if __name__ == '__main__':
    unittest.main()
