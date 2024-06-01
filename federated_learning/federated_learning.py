import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np

class FederatedLearningModel(nn.Module):
    def __init__(self):
        super(FederatedLearningModel, self).__init__()
        self.model = torchvision.models.resnet18(pretrained=False)
        self.model.fc = nn.Linear(512, 10)

    def forward(self, x):
        x = self.model(x)
        return x

class FederatedDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        data = self.data[idx]
        label = self.labels[idx]
        return data, label

def load_model():
    model = FederatedLearningModel()
    return model

def train_model(model, dataset, batch_size=32, epochs=10):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    for epoch in range(epochs):
        for batch in data_loader:
            inputs, labels = batch
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

def federated_learning_inference(model, input_data):
    model.eval()
    output = model(input_data)
    return output

def federated_learning_aggregate(models, weights=None):
    if weights is None:
        weights = [1/len(models) for _ in models]
    aggregated_model = models[0].state_dict()
    for k, v in aggregated_model.items():
        aggregated_model[k] = v.clone().detach().zero_()
    for i, model in enumerate(models):
        model_weight = weights[i]
        for k, v in model.state_dict().items():
            aggregated_model[k] += model_weight * v
    return aggregated_model
