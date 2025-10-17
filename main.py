import openml
import pandas as pd
dataset = openml.datasets.get_dataset(46938)
df, *_ = dataset.get_data()

wrngoewrgoiner