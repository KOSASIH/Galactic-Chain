import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class EdgeAI:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.model = None

    def build_model(self):
        model = Sequential([
            Dense(64, activation='relu', input_shape=(5,)),
            Dense(32, activation='relu'),
            Dense(2, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def train(self):
        self.model = self.build_model()
        self.model.fit(self.X, self.y, epochs=10)

    def evaluate(self, X_test, y_test):
        accuracy = self.model.evaluate(X_test, y_test)
        return accuracy
