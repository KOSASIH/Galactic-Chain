import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class SwarmLearning:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.models = []

    def build_model(self):
        model = LogisticRegression()
        return model

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        for i in range(5):
            model = self.build_model()
            model.fit(X_train, y_train)
            self.models.append(model)

    def evaluate(self, X_test, y_test):
        accuracy = 0
        for model in self.models:
            y_pred = model.predict(X_test)
            accuracy += accuracy_score(y_test, y_pred)
        return accuracy / len(self.models)
