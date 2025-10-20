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

# Data Transformation

df = pd.get_dummies(df, drop_first=True)
print(df.head())


# Select numeric columns (int or float)  #there are also uint8 and category types after get_dummies
numeric_columns = df.select_dtypes(include=['int64', 'float64','uint8','category']).columns.tolist()

# Select non-numeric columns 
non_numeric_columns = df.select_dtypes(exclude=['int64', 'float64','uint8','category']).columns.tolist()

# Convert all numeric columns to int64
df= df.astype(int)

print(df.info)

print(" Numerical Columns:")
for col in numeric_columns:
    print(" -", col)

print("\n Non-Numerical (Categorical) Columns:")
for col in non_numeric_columns:
    print(" -", col)



# Standardize numeric columns


# scaler = StandardScaler()
# df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

# SQL exploratory queries
pysqldf = lambda q: sqldf(q, globals())
query1 = """
SELECT region_1, AVG(credit_amount) AS avg_credit
FROM df
GROUP BY region_1
"""
result1 = pysqldf(query1)
print(result1)

plt.bar(result1['region_1'], result1['avg_credit'])
plt.title('Average Credit Amount by Region')
plt.xlabel('Regions 1 and 2')
plt.ylabel('Average Credit Amount')
plt.show()

