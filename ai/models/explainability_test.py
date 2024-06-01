import unittest
from tensorflow import keras
from galactic_chain.ai.models import Explainability, ExplainabilityModel

class TestExplainability(unittest.TestCase):
    def test_attention_visualization(self):
        model = keras.Sequential([keras.layers.Embedding(input_dim=100, output_dim=128), keras.layers.Attention()])
        explainability = Explainability(model)
        input_data = tf.random.normal((1, 10))
        attention_layer_name = 'attention'
        explainability.attention_visualization(input_data, attention_layer_name)

    def test_saliency_maps(self):
        model = keras.Sequential([keras.layers.Embedding(input_dim=100, output_dim=128), keras.layers.Dense(10)])
        explainability = Explainability(model)
        input_data = tf.random.normal((1, 10))
        class_index = 0
        explainability.saliency_maps(input_data, class_index)

    def test_feature_importance(self):
        model = keras.Sequential([keras.layers.Embedding(input_dim=100, output_dim=128), keras.layers.Dense(10)])
        explainability = Explainability(model)
        input_data = tf.random.normal((1, 10))
        num_features = 10
        explainability.feature_importance(input_data, num_features)

    def test_explainability_model(self):
        model = keras.Sequential([keras.layers.Embedding(input_dim=100, output_dim=128), keras.layers.Attention()])
        explainability_model = ExplainabilityModel(model)
        input_data = tf.random.normal((1, 10))
        attention_layer_name = 'attention'
        class_index = 0
        num_features = 10
        explainability_model.get_explainability(input_data, attention_layer_name, class_index, num_features)

if __name__ == '__main__':
    unittest.main()
