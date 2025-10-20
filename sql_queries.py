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