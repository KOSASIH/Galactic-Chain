import numpy as np
from sklearn.model_selection import GridSearchCV

class HyperparameterTuning:
    def __init__(self, model, data, target):
        self.model = model
        self.data = data
        self.target = target

    def grid_search(self, params):
        grid_search = GridSearchCV(self.model, params, cv=5)
        grid_search.fit(self.data, self.target)
        return grid_search.best_params_

    def random_search(self, params, n_iter):
        random_search = RandomizedSearchCV(self.model, params, cv=5, n_iter=n_iter)
        random_search.fit(self.data, self.target)
        return random_search.best_params_

    def bayesian_optimization(self, params, n_iter):
        # Implement Bayesian optimization using scikit-optimize or other libraries
        pass
