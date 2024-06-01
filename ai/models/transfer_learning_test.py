import unittest
from tensorflow import keras
from galactic_chain.ai.models import TransferLearning, TransferLearningModel

class TestTransferLearning(unittest.TestCase):
    def test_freeze_layers(self):
        pretrained_model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        model = keras.Sequential([keras.layers.Dense(5, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        transfer_learning = TransferLearning(model, pretrained_model)
        transfer_learning.freeze_layers(pretrained_model.layers[:-1])
        self.assertFalse(pretrained_model.layers[-1].trainable)

    def test_fine_tune(self):
        pretrained_model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        model = keras.Sequential([keras.layers.Dense(5, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        transfer_learning = TransferLearning(model, pretrained_model)
        transfer_learning.fine_tune(pretrained_model.layers[-1:], 10, 0.001)
        self.assertTrue(pretrained_model.layers[-1].trainable)

    def test_transfer_learning_model(self):
        pretrained_model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        model = keras.Sequential([keras.layers.Dense(5, input_shape=(10,), activation='relu'), keras.layers.Dense(1, activation='sigmoid')])
        transfer_learning_model = TransferLearningModel(model, pretrained_model)
        transfer_learning = transfer_learning_model.get_transfer_learning(pretrained_model.layers[:-1], pretrained_model.layers[-1:], 10, 0.001)
        self.assertIsInstance(transfer_learning, TransferLearning)

if __name__ == '__main__':
    unittest.main()
