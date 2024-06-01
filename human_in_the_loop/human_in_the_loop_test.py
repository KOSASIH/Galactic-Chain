import unittest
import torch
from human_in_the_loop import HumanInTheLoopModel, HumanInTheLoop

class TestHumanInTheLoop(unittest.TestCase):
    def test_human_in_the_loop(self):
        input_size = 10
        hidden_size = 5
        output_size = 3
        num_epochs = 10
        batch_size = 10
        num_queries = 2
        model = HumanInTheLoopModel(input_size, hidden_size, output_size)
        loss_fn = torch.nn.CrossEntropyLoss()
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        hital = HumanInTheLoop(model, loss_fn, optimizer, device)
        x = torch.randn(batch_size, input_size).to(device)
        y = torch.randint(0, output_size, (batch_size,)).to(device)
        for epoch in range(num_epochs):
            hital.train(x, y)
            x_query, y_query = hital.query(x, y, num_queries)
            hital.update(x_query, y_query)
        self.assertIsInstance(hital, HumanInTheLoop)

if __name__ == "__main__":
    unittest.main()
