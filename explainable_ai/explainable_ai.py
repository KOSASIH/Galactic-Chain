import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import shap

class ExplainableAIModel(nn.Module):
    def __init__(self):
        super(ExplainableAIModel, self).__init__()
        self.model = torchvision.models.resnet18(pretrained=False)
        self.model.fc = nn.Linear(512, 10)

    def forward(self, x):
        x = self.model(x)
        return x

def load_model():
    model = ExplainableAIModel()
    checkpoint = torch.load("explainable_ai_model.pt", map_location=torch.device("cpu"))
    model.load_state_dict(checkpoint)
    return model

def explain_model(model, input_data):
    model.eval()
    explainer = shap.DeepExplainer(model, input_data)
    shap_values = explainer.shap_values(input_data)
    return shap_values

def visualize_shap_values(shap_values, feature_names):
    shap.force_plot(None, shap_values, feature_names)

def explainable_ai_inference(model, input_data):
    shap_values = explain_model(model, input_data)
    visualize_shap_values(shap_values, feature_names)
    return shap_values

def edge_explainable_ai_inference(model, input_data):
    model.eval()
    output = model(input_data)
    shap_values = explain_model(model, input_data)
    return output, shap_values
