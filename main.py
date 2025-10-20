import openml
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pandasql import sqldf
import matplotlib.pyplot as plt
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

# DataIspectation
df.info()

print(df.describe())

print("Data base shape: ", df.shape)

duplicates = df.duplicated().sum()
print(f"Duplicates found: {duplicates}")


# Select numeric columns (int or float)  #there are also uint8 and category types after get_dummies
numeric_columns = df.select_dtypes(include=['int64', 'float64','uint8']).columns.tolist()

# Select non-numeric columns 
non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64','uint8']).columns.tolist()


print(" Numerical Columns:")
for col in numeric_columns:
    print(" -", col)

print("\n Non-Numerical (Categorical) Columns:")
for col in non_numeric_columns:
    print(" -", col)

# Data Transformation

df = pd.get_dummies(df, drop_first=True)
print(df.head())



# Convert all numeric columns to int64
df= df.astype(int)

print(df.info)

df.info()
print(df.head())
