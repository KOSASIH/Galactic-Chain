import numpy as np
import pandas as pd
from lime.lime_tabular import LimeTabularExplainer
from shap import TreeExplainer

class Explainability:
    def __init__(self, model, data, target):
        self.model = model
        self.data = data
        self.target = target

    def lime_explain(self, instance):
        explainer = LimeTabularExplainer(self.data.values, feature_names=self.data.columns, class_names=self.target.unique())
        exp = explainer.explain_instance(instance, self.model.predict_proba, num_features=5)
        return exp.as_list()

    def shap_explain(self, instance):
        explainer = TreeExplainer(self.model)
        shap_values = explainer.shap_values(instance)
        return shap_values

    def tree_explain(self, instance):
        explainer = TreeExplainer(self.model)
        tree_explanation = explainer.explain_instance(instance, self.model.predict_proba)
        return tree_explanation
