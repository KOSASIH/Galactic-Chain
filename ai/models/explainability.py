import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class Explainability:
    def __init__(self, model):
        self.model = model

    def attention_visualization(self, input_data, attention_layer_name):
        attention_layer = self.model.get_layer(attention_layer_name)
        attention_weights = attention_layer.get_weights()[0]
        attention_weights = tf.squeeze(attention_weights, axis=0)
        attention_weights = attention_weights.numpy()

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(attention_weights, cmap='viridis')
        ax.set_title('Attention Weights')
        ax.set_xlabel('Input Tokens')
        ax.set_ylabel('Attention Heads')
        plt.show()

    def saliency_maps(self, input_data, class_index):
        gradients = tf.gradients(self.model.output[0, class_index], input_data)[0]
        gradients = tf.abs(gradients)
        gradients = gradients / tf.reduce_max(gradients)

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.imshow(gradients, cmap='viridis')
        ax.set_title('Saliency Map')
        ax.set_xlabel('Input Features')
        ax.set_ylabel('Saliency')
        plt.show()

    def feature_importance(self, input_data, num_features):
        feature_importances = []
        for i in range(num_features):
            feature_importance = tf.gradients(self.model.output, input_data[:, i])[0]
            feature_importance = tf.abs(feature_importance)
            feature_importance = feature_importance / tf.reduce_max(feature_importance)
            feature_importances.append(feature_importance)

        feature_importances = tf.stack(feature_importances, axis=0)
        feature_importances = feature_importances.numpy()

        fig, ax = plt.subplots(figsize=(10, 10))
        ax.bar(range(num_features), feature_importances)
        ax.set_title('Feature Importance')
        ax.set_xlabel('Feature Index')
        ax.set_ylabel('Importance')
        plt.show()

class ExplainabilityModel(keras.Model):
    def __init__(self, model):
        super(ExplainabilityModel, self).__init__()
        self.model = model

    def call(self, inputs):
        outputs = self.model(inputs)
        return outputs

    def get_explainability(self, input_data, attention_layer_name, class_index, num_features):
        explainability = Explainability(self.model)
        explainability.attention_visualization(input_data, attention_layer_name)
        explainability.saliency_maps(input_data, class_index)
        explainability.feature_importance(input_data, num_features)
