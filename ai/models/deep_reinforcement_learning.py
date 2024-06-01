import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten

class DeepQNetwork:
    def __init__(self, state_dim, action_dim, learning_rate=0.001, discount_factor=0.99):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.model = self.create_model()

    def create_model(self):
        model = Sequential()
        model.add(Conv2D(32, (8, 8), activation='relu', input_shape=(self.state_dim, self.state_dim, 1)))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dense(self.action_dim, activation='linear'))
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)
        self.next_states.append(next_state)
        self.dones.append(done)

    def train(self, batch_size):
        state_batch, action_batch, reward_batch, next_state_batch, done_batch = self.sample_memory(batch_size)
        target_q_values = reward_batch + self.discount_factor * np.max(self.model.predict(next_state_batch), axis=1)
        target_q_values[done_batch] = reward_batch[done_batch]
        self.model.fit(state_batch, target_q_values, verbose=0)

    def act(self, state):
        state = np.expand_dims(state, axis=0)
        q_values = self.model.predict(state)
        action = np.argmax(q_values)
        return action

    def sample_memory(self, batch_size):
        indices = np.random.choice(len(self.states), batch_size)
        state_batch = np.array(self.states)[indices]
        action_batch = np.array(self.actions)[indices]
        reward_batch = np.array(self.rewards)[indices]
        next_state_batch = np.array(self.next_states)[indices]
        done_batch = np.array(self.dones)[indices]
        return state_batch, action_batch, reward_batch, next_state_batch, done_batch

    def save(self, filepath):
        self.model.save(filepath)

    def load(self, filepath):
        self.model = tf.keras.models.load_model(filepath)
