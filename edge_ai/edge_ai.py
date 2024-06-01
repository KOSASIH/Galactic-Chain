import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
import numpy as np

class EdgeAIModel(nn.Module):
    def __init__(self):
        super(EdgeAIModel, self).__init__()
        self.model = torchvision.models.resnet18(pretrained=False)
        self.model.fc = nn.Linear(512, 10)

    def forward(self, x):
        x = self.model(x)
        return x

class EdgeAIDataset(Dataset):
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
    model = EdgeAIModel()
    checkpoint = torch.load("edge_ai_model.pt", map_location=torch.device("cpu"))
    model.load_state_dict(checkpoint)
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

def predict(model, input_data):
    model.eval()
    output = model(input_data)
    return output.argmax(dim=1)

def edge_ai_inference(model, input_data):
    output = predict(model, input_data)
    return output
