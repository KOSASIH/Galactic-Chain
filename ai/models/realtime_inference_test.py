import unittest
from tensorflow import keras
from galactic_chain.ai.models import RealtimeInference, RealtimeInferenceModel

class TestRealtimeInference(unittest.TestCase):
    def test_optimize_model(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        batch_size = 32
        latency_constraint = 10
        realtime_inference = RealtimeInference(model, batch_size, latency_constraint)
        interpreter = realtime_inference.optimize_model()
        self.assertIsInstance(interpreter, tf.lite.Interpreter)

    def test_inference(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        batch_size = 32
        latency_constraint = 10
        realtime_inference = RealtimeInference(model, batch_size, latency_constraint)
        input_data = np.random.rand(1, 10)
        output_data = realtime_inference.inference(input_data)
        self.assertIsInstance(output_data, np.ndarray)

    def test_realtime_inference_model(self):
        model = keras.Sequential([keras.layers.Dense(10, input_shape=(10,), activation='relu'), keras.layers.Dense(5, activation='relu')])
        batch_size = 32
        latency_constraint = 10
        realtime_inference_model = RealtimeInferenceModel(model, batch_size, latency_constraint)
        realtime_inference = realtime_inference_model.get_realtime_inference()
        self.assertIsInstance(realtime_inference, RealtimeInference)

if __name__ == '__main__':
    unittest.main()
