import unittest
from galactic_chain.ai.models import NLPModel, LanguageModel, TextClassifier

class TestNLPModel(unittest.TestCase):
    def test_create_model(self):
        nlp_model = NLPModel(vocab_size=1000, embedding_dim=128, hidden_dim=256, output_dim=128)
        self.assertIsInstance(nlp_model.model, tf.keras.engine.training.Model)

    def test_train(self):
        nlp_model = NLPModel(vocab_size=1000, embedding_dim=128, hidden_dim=256, output_dim=128)
        X_train = np.random.randint(0, 1000, size=(100, 10))
        y_train = np.random.randint(0, 128, size=(100, 10))
        X_val = np.random.randint(0, 1000, size=(20, 10))
        y_val = np.random.randint(0, 128, size=(20, 10))
        nlp_model.train(X_train, y_train, X_val, y_val)

    def test_predict(self):
        nlp_model = NLPModel(vocab_size=1000, embedding_dim=128, hidden_dim=256, output_dim=128)
        X_test = np.random.randint(0, 1000, size=(10, 10))
        output = nlp_model.predict(X_test)
        self.assertIsInstance(output, np.ndarray)

class TestLanguageModel(unittest.TestCase):
    def test_generate_text(self):
        language_model = LanguageModel(vocab_size=1000, embedding_dim=128, hidden_dim=256, output_dim=128)
        seed_text = "This is a test"
        num_words = 10
        output_text = language_model.generate_text(seed_text, num_words)
        self.assertIsInstance(output_text, str)

class TestTextClassifier(unittest.TestCase):
    def test_classify_text(self):
        text_classifier = TextClassifier(vocab_size=1000, embedding_dim=128, hidden_dim=256, output_dim=128)
        input_text = "This is a test"
        output = text_classifier.classify_text(input_text)
        self.assertIsInstance(output, np.ndarray)

if __name__ == '__main__':
    unittest.main()
