import pandas as pd
from typing import List, Dict

# Load and preprocess data
df = pd.read_csv('https://plotly.github.io/datasets/iris.csv')
df = df.rename(columns={"Name": "Species"})

# Create options for dropdowns
opts1: List[Dict[str, str]] = [
    {'label': i, 'value': i} for i in df.iloc[:, [0, 1, 2, 3]]
]
opts3: List[Dict[str, str]] = [
    {'label': i, 'value': i} for i in df.iloc[:, [0, 1, 2, 3, 4]]
] 