import unittest
from galactic_chain.model_serving import ModelServing

class TestModelServing(unittest.TestCase):
    def setUp(self):
        self.model = lambda x: x

    def test_deploy_model(self):
        model_serving = ModelServing(self.model)
        model_serving.deploy_model('localhost', 8500)

if __name__ == '__main__':
    unittest.main()
