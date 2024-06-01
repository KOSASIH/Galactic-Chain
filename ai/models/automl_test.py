from galactic_chain.ai.models.automl import AutoML

def test_automl():
    X = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    y = [0, 1, 0, 1]

    automl = AutoML(X, y)
    automl.train()
    accuracy = automl.evaluate(X, y)
    assert accuracy >= 0.5, "The accuracy of the model is low"

if __name__ == '__main__':
    test_automl()
