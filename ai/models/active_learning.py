import numpy as np
import tensorflow as tf

class ActiveLearning:
    def __init__(self, model, data_manager):
        self.model = model
        self.data_manager = data_manager

    def uncertainty_sampling(self, num_samples):
        """
        Selects the top `num_samples` data points with the highest uncertainty.
        """
        uncertainty_values = []
        for i in range(len(self.data_manager.data)):
            input_data = self.data_manager.data[i]
            output_probabilities = self.model.predict(input_data)[0]
            uncertainty_value = -np.max(np.log(output_probabilities))
            uncertainty_values.append(uncertainty_value)

        sorted_indices = np.argsort(uncertainty_values)[-num_samples:]
        selected_indices = sorted_indices[np.argsort(np.random.rand(len(sorted_indices)))]
        selected_data = [self.data_manager.data[i] for i in selected_indices]
        return selected_data

    def query_by_committee(self, num_samples):
        """
        Selects the top `num_samples` data points with the highest disagreement between a committee of models.
        """
        committee_models = [self.model.copy() for _ in range(5)]
        uncertainty_values = []
        for i in range(len(self.data_manager.data)):
            input_data = self.data_manager.data[i]
            committee_outputs = []
            for committee_model in committee_models:
                committee_output = committee_model.predict(input_data)[0]
                committee_outputs.append(committee_output)
            committee_outputs = np.array(committee_outputs)
            uncertainty_value = np.std(committee_outputs, axis=0)[-1]
            uncertainty_values.append(uncertainty_value)

        sorted_indices = np.argsort(uncertainty_values)[-num_samples:]
        selected_indices = sorted_indices[np.argsort(np.random.rand(len(sorted_indices)))]
        selected_data = [self.data_manager.data[i] for i in selected_indices]
        return selected_data

class ActiveLearningModel(keras.Model):
    def __init__(self, model, data_manager):
        super(ActiveLearningModel, self).__init__()
        self.model = model
        self.data_manager = data_manager

    def call(self, inputs):
        outputs = self.model(inputs)
        return outputs

    def get_active_learning_data(self, num_samples, strategy):
        active_learning = ActiveLearning(self.model, self.data_manager)
        if strategy == 'uncertainty_sampling':
            selected_data = active_learning.uncertainty_sampling(num_samples)
        elif strategy == 'query_by_committee':
            selected_data = active_learning.query_by_committee(num_samples)
        else:
            raise ValueError('Invalid active learning strategy')
        return selected_data
