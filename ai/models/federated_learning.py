import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow_federated.python.core.api import computation_types
from tensorflow_federated.python.core.api import computations
from tensorflow_federated.python.core.api import intrinsics
from tensorflow_federated.python.core.api import placements

class FederatedLearning:
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
        federated_data = tf.data.Dataset.from_tensor_slices((self.X, self.y))
        federated_data = federated_data.batch(4)
        federated_data = federated_data.prefetch(tf.data.AUTOTUNE)

        @computations.tf_computation(computation_types.SequenceType(tf.float32))
        def train_model(model, data):
            for x, y in data:
                with tf.GradientTape() as tape:
                    y_pred = model(x, training=True)
                    loss = tf.reduce_mean(tf.keras.losses.sparse_categorical_crossentropy(y, y_pred))
                gradients = tape.gradient(loss, model.trainable_variables)
                optimizer = tf.keras.optimizers.Adam()
                optimizer.apply_gradients(zip(gradients, model.trainable_variables))
            return model

        @computations.tf_computation(computation_types.SequenceType(tf.float32))
        def evaluate_model(model, data):
            accuracy = tf.keras.metrics.Accuracy()
            for x, y in data:
                y_pred = model(x, training=False)
                accuracy.update_state(y, y_pred)
            return accuracy.result()

        @computations.federated_computation()
        def federated_train(model, data):
            return intrinsics.federated_map(train_model, (model, data))

        @computations.federated_computation()
        def federated_evaluate(model, data):
            return intrinsics.federated_map(evaluate_model, (model, data))

        self.model = federated_train(self.model, federated_data)
        accuracy = federated_evaluate(self.model, federated_data)
        return accuracy
