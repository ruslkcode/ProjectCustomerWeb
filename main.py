import openml
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pandasql import sqldf
import matplotlib.pyplot as plt
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

# DataInspectation
df.info()

print(df.describe())

print("Data base shape: ", df.shape)

duplicates = df.duplicated().sum()
print(f"Duplicates found: {duplicates}")

# Data Transformation

df = pd.get_dummies(df, drop_first=True)
print(df.head())

df=df.astype(int)

df.info()
