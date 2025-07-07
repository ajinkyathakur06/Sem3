import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

name ='tips'
data = sns.load_dataset(name)

# print(data.head())
# print(data.shape)
# print(data.info())
# print(data.describe())

print(data.select_dtypes(include='category'))


for col in data.select_dtypes(include='category').columns:
    print(col,"=",data[col].unique())
    print()
