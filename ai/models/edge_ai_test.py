from galactic_chain.ai.models.edge_ai import EdgeAI

def test_edge_ai():
    X = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    y = [0, 1, 0, 1]

    edge_ai = EdgeAI(X, y)
    edge_ai.train()
    accuracy = edge_ai.evaluate(X, y)
    assert accuracy >= 0.5, "The accuracy of the model is low"

if __name__ == '__main__':
    test_edge_ai()
