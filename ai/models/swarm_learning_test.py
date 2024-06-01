from galactic_chain.ai.models.swarm_learning import SwarmLearning

def test_swarm_learning():
    X = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    y = [0, 1, 0, 1]

    swarm_learning = SwarmLearning(X, y)
    swarm_learning.train()
    accuracy = swarm_learning.evaluate(X, y)
    assert accuracy >= 0.5, "The accuracy of the model is low"

if __name__ == '__main__':
    test_swarm_learning()
