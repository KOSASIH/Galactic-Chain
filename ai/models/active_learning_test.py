import unittest
from tensorflow import keras
from galactic_chain.ai.models import ActiveLearning, ActiveLearningModel

class TestActiveLearning(unittest.TestCase):
    def test_uncertainty_sampling(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        data_manager = DataManager(data=[np.random.normal((10,)) for _ in range(100)], labels=[0 for _ in range(100)])
        active_learning = ActiveLearning(model, data_manager)
        selected_data = active_learning.uncertainty_sampling(10)
        self.assertEqual(len(selected_data), 10)

    def test_query_by_committee(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        data_manager = DataManager(data=[np.random.normal((10,)) for _ in range(100)], labels=[0 for _ in range(100)])
        active_learning = ActiveLearning(model, data_manager)
        selected_data = active_learning.query_by_committee(10)
        self.assertEqual(len(selected_data), 10)

    def test_active_learning_model(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        data_manager = DataManager(data=[np.random.normal((10,)) for _ in range(100)], labels=[0 for _ in range(100)])
        active_learning_model = ActiveLearningModel(model, data_manager)
        selected_data = active_learning_model.get_active_learning_data(10, 'uncertainty_sampling')
        self.assertEqual(len(selected_data), 10)

if __name__ == '__main__':
    unittest.main()
