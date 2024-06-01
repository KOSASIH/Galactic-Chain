import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Embedding, LSTM, Dense

class NLPModel:
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim
        self.output_dim = output_dim
        self.model = self.create_model()

    def create_model(self):
        input_layer = tf.keras.layers.Input(shape=(None,))
        embedding_layer = Embedding(self.vocab_size, self.embedding_dim, input_length=None)(input_layer)
        lstm_layer = LSTM(self.hidden_dim)(embedding_layer)
        output_layer = Dense(self.output_dim, activation='softmax')(lstm_layer)
        model = Model(inputs=input_layer, outputs=output_layer)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, X_val, y_val):
        self.model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)

    def predict(self, X_test):
        return self.model.predict(X_test)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)

class LanguageModel(NLPModel):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(LanguageModel, self).__init__(vocab_size, embedding_dim, hidden_dim, output_dim)

    def generate_text(self, seed_text, num_words):
        input_seq = tf.keras.preprocessing.text.text_to_word_sequence(seed_text)
        output_seq = []
        for i in range(num_words):
            input_seq_tensor = tf.convert_to_tensor([input_seq])
            output = self.model.predict(input_seq_tensor)
            output_word = tf.argmax(output, axis=1)
            output_seq.append(output_word)
            input_seq = input_seq[1:] + [output_word]
        return ' '.join(output_seq)

class TextClassifier(NLPModel):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(TextClassifier, self).__init__(vocab_size, embedding_dim, hidden_dim, output_dim)

    def classify_text(self, input_text):
        input_seq = tf.keras.preprocessing.text.text_to_word_sequence(input_text)
        input_seq_tensor = tf.convert_to_tensor([input_seq])
        output = self.model.predict(input_seq_tensor)
        return tf.argmax(output, axis=1)
