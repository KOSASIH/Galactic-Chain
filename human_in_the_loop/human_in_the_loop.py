import torch
import numpy as np
import random

class HumanInTheLoopModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(HumanInTheLoopModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

class HumanInTheLoop:
    def __init__(self, model, loss_fn, optimizer, device):
        self.model = model
        self.loss_fn = loss_fn
        self.optimizer = optimizer
        self.device = device

    def train(self, x, y):
        self.model.train()
        x, y = x.to(self.device), y.to(self.device)
        y_pred = self.model(x)
        loss = self.loss_fn(y_pred, y)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

    def predict(self, x):
        self.model.eval()
        x = x.to(self.device)
        y_pred = self.model(x)
        return y_pred

    def query(self, x, y, n):
        self.model.eval()
        x, y = x.to(self.device), y.to(self.device)
        y_pred = self.model(x)
        _, indices = torch.topk(y_pred, n, dim=1, largest=False)
        return x[torch.arange(x.shape[0]).unsqueeze(1), indices], y[torch.arange(x.shape[0]).unsqueeze(1), indices]

    def update(self, x, y):
        self.train(x, y)

def main(input_size, hidden_size, output_size, num_epochs, batch_size, num_queries):
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

if __name__ == "__main__":
    input_size = 10
    hidden_size = 5
    output_size = 3
    num_epochs = 10
    batch_size = 10
    num_queries = 2
    main(input_size, hidden_size, output_size, num_epochs, batch_size, num_queries)
