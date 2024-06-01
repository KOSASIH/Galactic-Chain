import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input

class ReinforcementLearning:
    def __init__(self, state_dim, action_dim, gamma=0.99, alpha=0.01):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.gamma = gamma
        self.alpha = alpha
        self.model = self.create_model()

    def create_model(self):
        state_input = Input(shape=(self.state_dim,))
        x = Dense(64, activation='relu')(state_input)
        x = Dense(64, activation='relu')(x)
        action_output = Dense(self.action_dim, activation='softmax')(x)
        model = Model(inputs=state_input, outputs=action_output)
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        return model

    def get_action(self, state):
        state = np.array(state).reshape(1, -1)
        action_probs = self.model.predict(state)
        action = np.random.choice(self.action_dim, p=action_probs[0])
        return action

    def update(self, state, action, reward, next_state, done):
        state = np.array(state).reshape(1, -1)
        next_state = np.array(next_state).reshape(1, -1)
        action_onehot = np.zeros(self.action_dim)
        action_onehot[action] = 1
        target = reward + self.gamma * np.max(self.model.predict(next_state)[0])
        self.model.fit(state, action_onehot, epochs=1, verbose=0)
        self.model.fit(next_state, action_onehot, epochs=1, verbose=0)

    def save(self, filename):
        self.model.save(filename)

    def load(self, filename):
        self.model = tf.keras.models.load_model(filename)

class QLearning(ReinforcementLearning):
    def __init__(self, state_dim, action_dim, gamma=0.99, alpha=0.01):
        super(QLearning, self).__init__(state_dim, action_dim, gamma, alpha)

    def update(self, state, action, reward, next_state, done):
        state = np.array(state).reshape(1, -1)
        next_state = np.array(next_state).reshape(1, -1)
        q_values = self.model.predict(state)[0]
        q_values[action] = reward + self.gamma * np.max(self.model.predict(next_state)[0])
        self.model.fit(state, q_values, epochs=1, verbose=0)

class DeepQLearning(ReinforcementLearning):
    def __init__(self, state_dim, action_dim, gamma=0.99, alpha=0.01):
        super(DeepQLearning, self).__init__(state_dim, action_dim, gamma, alpha)

    def create_model(self):
        state_input = Input(shape=(self.state_dim,))
        x = Dense(64, activation='relu')(state_input)
        x = Dense(64, activation='relu')(x)
        q_values = Dense(self.action_dim)(x)
        model = Model(inputs=state_input, outputs=q_values)
        model.compile(optimizer='adam', loss='mse')
        return model

    def update(self, state, action, reward, next_state, done):
        state = np.array(state).reshape(1, -1)
        next_state = np.array(next_state).reshape(1, -1)
        q_values = self.model.predict(state)[0]
        q_values[action] = reward + self.gamma * np.max(self.model.predict(next_state)[0])
        self.model.fit(state, q_values, epochs=1, verbose=0)
