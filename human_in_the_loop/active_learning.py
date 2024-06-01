import torch
import numpy as np

def uncertainty_sampling(model, x, y, n):
    model.eval()
    with torch.no_grad():
        y_pred = model(x)
        _, indices = torch.topk(torch.nn.functional.softmax(y_pred, dim=1), n, dim=1, largest=False)
    return x[torch.arange(x.shape[0]).unsqueeze(1), indices], y[torch.arange(x.shape[0]).unsqueeze(1), indices]

def query_by_committee(models, x, y, n):
    model_preds = [model(x) for model in models]
    model_preds = torch.stack(model_preds, dim=0)
    model_preds = torch.nn.functional.softmax(model_preds, dim=1)
    model_preds = torch.mean(model_preds, dim=0)
    _, indices = torch.topk(model_preds, n, dim=1, largest=False)
    return x[torch.arange(x.shape[0]).unsqueeze(1), indices], y[torch.arange(x.shape[0]).unsqueeze(1), indices]

def coreset_sampling(model, x, y, n):
    model.eval()
    with torch.no_grad():
        y_pred = model(x)
        y_pred = torch.nn.functional.softmax(y_pred, dim=1)
        distances = torch.cdist(y_pred, y_pred)
        distances = torch.triu(distances, diagonal=1)
        distances = torch.sum(distances, dim=1)
        _, indices = torch.topk(distances, n)
    return x[indices], y[indices]

def main(input_size, hidden_size, output_size, num_epochs, batch_size, num_queries, query_strategy):
    model = HumanInTheLoopModel(input_size, hidden_size, output_size)
    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    if query_strategy == "uncertainty_sampling":
        query_fn = uncertainty_sampling
    elif query_strategy == "query_by_committee":
        models = [HumanInTheLoopModel(input_size, hidden_size, output_size) for _ in range(5)]
        for model in models:
            model.to(device)
        query_fn = query_by_committee
    elif query_strategy == "coreset_sampling":
        query_fn= coreset_sampling
    else:
        raise ValueError("Invalid query strategy")
    x = torch.randn(batch_size, input_size).to(device)
    y = torch.randint(0, output_size, (batch_size,)).to(device)
    for epoch in range(num_epochs):
        x_query, y_query = query_fn(model, x, y, num_queries)
        optimizer.zero_grad()
        y_pred = model(x_query)
        loss = loss_fn(y_pred, y_query)
        loss.backward()
        optimizer.step()

if __name__ == "__main__":
    input_size = 10
    hidden_size = 5
    output_size = 3
    num_epochs = 10
    batch_size = 10
    num_queries = 2
    query_strategy = "uncertainty_sampling"
    main(input_size, hidden_size, output_size, num_epochs, batch_size, num_queries, query_strategy)
