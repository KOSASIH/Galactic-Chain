from galactic_chain.ai.models.autokeras import AutoKeras

def test_autokeras():
    X = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    y = [0, 1, 0, 1]

   autokeras = AutoKeras(X, y)
    autokeras.train()
    accuracy = autokeras.evaluate(X, y)
    assert accuracy >= 0.5, "The accuracy of the model is low"

if __name__ == '__main__':
    test_autokeras()
