import unittest
from tensorflow import keras
from galactic_chain.ai.models import MultiModalModel

class TestMultiModalModel(unittest.TestCase):
    def test_model_creation(self):
        num_classes = 10
        text_embedding_dim = 128
        image_embedding_dim = 128
        audio_embedding_dim = 128
        model = MultiModalModel(num_classes, text_embedding_dim, image_embedding_dim, audio_embedding_dim)
        self.assertIsInstance(model, keras.Model)

    def test_model_call(self):
        num_classes = 10
        text_embedding_dim = 128
        image_embedding_dim = 128
        audio_embedding_dim = 128
        model = MultiModalModel(num_classes, text_embedding_dim, image_embedding_dim, audio_embedding_dim)
        text_input = tf.random.normal((1, 10))
        image_input = tf.random.normal((1, 28, 28, 3))
        audio_input = tf.random.normal((1, 10, 128))
        output = model([text_input, image_input, audio_input])
        self.assertEqual(output.shape, (1, num_classes))

    def test_text_encoder(self):
        text_embedding_dim = 128
        text_encoder = TextEncoder(text_embedding_dim)
        text_input = tf.random.normal((1, 10))
        output = text_encoder(text_input)
        self.assertEqual(output.shape, (1, 128))

    def test_image_encoder(self):
        image_embedding_dim = 128
        image_encoder = ImageEncoder(image_embedding_dim)
        image_input = tf.random.normal((1, 28, 28, 3))
        output = image_encoder(image_input)
        self.assertEqual(output.shape, (1, 128))

    def test_audio_encoder(self):
        audio_embedding_dim = 128
        audio_encoder = AudioEncoder(audio_embedding_dim)
        audio_input = tf.random.normal((1, 10, 128))
        output = audio_encoder(audio_input)
        self.assertEqual(output.shape, (1, 128))

if __name__ == '__main__':
    unittest.main()
