import unittest
from galactic_chain.ai.models import ReinforcementLearning, QLearning, DeepQLearning

class TestReinforcementLearning(unittest.TestCase):
    def test_get_action(self):
        rl = ReinforcementLearning(state_dim=4, action_dim=2)
        state = np.random.rand(4)
        action = rl.get_action(state)
        self.assertIsInstance(action, int)

    def test_update(self):
        rl = ReinforcementLearning(state_dim=4, action_dim=2)
        state = np.random.rand(4)
        action = 0
        reward = 1
        next_state = np.random.rand(4)
        done = False
        rl.update(state, action, reward, next_state, done)

    def test_save_load(self):
        rl = ReinforcementLearning(state_dim=4, action_dim=2)
        rl.save('test_model.h5')
        rl_load = ReinforcementLearning(state_dim=4, action_dim=2)
        rl_load.load('test_model.h5')

class TestQLearning(unittest.TestCase):
    def test_update(self):
        ql = QLearning(state_dim=4, action_dim=2)
        state = np.random.rand(4)
        action = 0
        reward = 1
        next_state = np.random.rand(4)
        done = False
        ql.update(state, action, reward, next_state, done)

class TestDeepQLearning(unittest.TestCase):
    def test_update(self):
        dql = DeepQLearning(state_dim=4, action_dim=2)
        state = np.random.rand(4)
        action = 0
        reward = 1
        next_state = np.random.rand(4)
        done = False
        dql.update(state, action, reward, next_state, done)

if __name__ == '__main__':
    unittest.main()
