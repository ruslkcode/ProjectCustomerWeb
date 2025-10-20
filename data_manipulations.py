import openml
import pandas as pd
from sklearn.preprocessing import StandardScaler
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

# DataIspectation

df.info()

print(df.describe())

print("Data base shape: ", df.shape)

duplicates = df.duplicated().sum()
print(f"Duplicates found: {duplicates}")

# Data Transformation

df = pd.get_dummies(df, drop_first=True)
print(df.head())

# Select numeric columns (int or float)
numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

# Select non-numeric columns 
non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64']).columns.tolist()

print(" Numerical Columns:")
for col in numeric_columns:
    print(" -", col)

print("\n Non-Numerical (Categorical) Columns:")
for col in non_numeric_columns:
    print(" -", col)

scaler = StandardScaler()
df[numeric_columns] = scaler.fit_transform(df[numeric_columns])