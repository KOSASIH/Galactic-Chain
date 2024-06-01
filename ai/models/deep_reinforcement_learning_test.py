import unittest
import numpy as np
from galactic_chain.ai.models import DeepQNetwork

class TestDeepQNetwork(unittest.TestCase):
    def test_create_model(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        self.assertIsInstance(dqn.model, tf.keras.engine.training.Model)

    def test_remember(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        state = np.random.rand(4, 4, 1)
        action = 0
        reward = 1
        next_state = np.random.rand(4, 4, 1)
        done = False
        dqn.remember(state, action, reward, next_state, done)
        self.assertEqual(len(dqn.states), 1)

    def test_train(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        states = np.random.rand(10, 4, 4, 1)
        actions = np.random.randint(0, 2, size=10)
        rewards = np.random.rand(10)
        next_states = np.random.rand(10, 4, 4, 1)
        dones = np.random.randint(0, 2, size=10)
        dqn.states = states
        dqn.actions = actions
        dqn.rewards = rewards
        dqn.next_states = next_states
        dqn.dones = dones
        dqn.train(batch_size=5)

    def test_act(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        state = np.random.rand(4, 4, 1)
        action = dqn.act(state)
        self.assertIsInstance(action, int)

    def test_sample_memory(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        states = np.random.rand(10, 4, 4, 1)
        actions = np.random.randint(0, 2, size=10)
        rewards = np.random.rand(10)
        next_states = np.random.rand(10, 4, 4, 1)
        dones = np.random.randint(0, 2, size=10)
        dqn.states = states
        dqn.actions = actions
        dqn.rewards = rewards
        dqn.next_states = next_states
        dqn.dones = dones
        state_batch, action_batch, reward_batch, next_state_batch, done_batch = dqn.sample_memory(batch_size=5)
        self.assertEqual(len(state_batch), 5)

    def test_save_load(self):
        dqn = DeepQNetwork(state_dim=4, action_dim=2)
        filepath = "test_dqn.h5"
        dqn.save(filepath)
        dqn_loaded = DeepQNetwork(state_dim=4, action_dim=2)
        dqn_loaded.load(filepath)
        self.assertTrue(np.allclose(dqn.model.get_weights(), dqn_loaded.model.get_weights()))
