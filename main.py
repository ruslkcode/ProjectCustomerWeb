import openml
import pandas as pd
from sklearn.preprocessing import StandardScaler
from pandasql import sqldf
import matplotlib.pyplot as plt
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()


