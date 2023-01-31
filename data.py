import pandas as pd

df = pd.read_csv('https://plotly.github.io/datasets/iris.csv') 
df = df.rename(columns={"Name": "Species"}) 

opts1 = [{'label' : i, 'value' : i} for i in df.iloc[:,[0,1,2,3]]] 
opts3 = [{'label' : i, 'value' : i} for i in df.iloc[:,[0,1,2,3,4]]] 