import pandas as pd
from sklearn.preprocessing import StandardScaler

class DataQuality:
    def __init__(self, data):
        self.data = data

    def clean_data(self):
        self.data.dropna(inplace=True)
        self.data.drop_duplicates(inplace=True)
        return self.data

    def validate_data(self):
        for col in self.data.columns:
            if self.data[col].dtype == 'object':
                self.data[col] = self.data[col].apply(lambda x: x.strip())
        return self.data

    def normalize_data(self):
        scaler = StandardScaler()
        self.data[['numeric_col1', 'numeric_col2']] = scaler.fit_transform(self.data[['numeric_col1', 'numeric_col2']])
        return self.data
