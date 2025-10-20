import openml
from pandasql import sqldf
import matplotlib.pyplot as plt
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

# SQL exploratory queries

pysqldf = lambda q: sqldf(q, globals())
query1 = """
SELECT region, AVG(credit_amount) AS avg_credit
FROM df
GROUP BY region
"""
result1 = pysqldf(query1)
print(result1)

plt.bar(result1['region'], result1['avg_credit'])
plt.title('Average Credit Amount by Region')
plt.xlabel('Regions 1 and 2')
plt.ylabel('Average Credit Amount')
plt.show()

query2 = """
SELECT age, credit_amount
FROM df
GROUP BY age
"""
result2 = pysqldf(query2)
print(result2)

plt.scatter(result2['age'], result2['credit_amount'], alpha=0.6)
plt.title('Relationship between Age and Credit Amount')
plt.xlabel('Age')
plt.ylabel('Credit Amount')
plt.show()

query3 = """
SELECT product_type,
       AVG(credit_amount) AS avg_credit,
       AVG(income) AS avg_income
FROM df
GROUP BY product_type
ORDER BY avg_credit DESC
"""
result3 = pysqldf(query3)
print(result3)

plt.figure(figsize=(8,6))
plt.barh(result3['product_type'], result3['avg_credit'])
plt.title('Average Credit Amount by Product Type')
plt.xlabel('Average Credit Amount')
plt.ylabel('Product Type')
plt.tight_layout()
plt.show()