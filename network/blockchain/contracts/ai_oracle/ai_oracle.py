import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class AIOracle:
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.model = RandomForestClassifier(n_estimators=100)

    def train(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))

    def predict(self, input_data):
        return self.model.predict(input_data)

    def update(self, new_data, new_target):
        self.data = np.concatenate((self.data, new_data))
        self.target = np.concatenate((self.target, new_target))
        self.train()
