import autokeras as ak

class AutoKeras:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.model = None

    def build_model(self):
        model = ak.ImageClassifier(
            max_trials=10,
            overwrite=True,
            directory='./tmp'
        )
        return model

    def train(self):
        self.model = self.build_model()
        self.model.fit(self.X, self.y, epochs=10)

    def evaluate(self, X_test, y_test):
        accuracy = self.model.evaluate(X_test, y_test)
        return accuracy
