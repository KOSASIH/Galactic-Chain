import torch
import torch.nn as nn
import torch.quantization

def model_quantization(model):
    model.eval()
    torch.quantization.quantize_dynamic(model, {torch.nn.Linear, torch.nn.Conv2d}, dtype=torch.qint8)

def model_pruning(model, amount=0.2):
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Conv2d) or isinstance(module, torch.nn.Linear):
            weight_copy = module.weight.data.abs().clone()
            _, idx = torch.sort(weight_copy)
            _, mask = torch.sort(idx, descending=True)
            mask = mask[:int(amount * mask.shape[0])]
            module.weight.data[mask] = 0

def model_knowledge_distillation(student, teacher, dataset, batch_size=32, epochs=10):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    student.to(device)
    teacher.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(student.parameters(), lr=0.001)
    data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    for epoch in range(epochs):
        for batch in data_loader:
            inputs, labels = batch
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            student_outputs = student(inputs)
            teacher_outputs = teacher(inputs)
            loss = criterion(student_outputs, labels) + 0.5 * criterion(student_outputs, teacher_outputs)
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

def compress_model(model):
    model_quantization(model)
    model_pruning(model)
    return model
