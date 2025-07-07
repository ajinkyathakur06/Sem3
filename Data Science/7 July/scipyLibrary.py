import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Read the CSV
df = pd.read_csv('Data Science/StudentsPerformance.csv')

# Add a new column: average score
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

males_scores = df[df['gender'] == 'male']['average_score']
females_scores = df[df['gender'] == 'female']['average_score']

t_stat, p_value = stats.ttest_ind(males_scores, females_scores)
print(f"T-statistic: {t_stat}, P-value: {p_value}")

X = df[['reading score', 'writing score']]
y = df['math score']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model coefficients: {model.coef_}")
print("r^2 score:", model.score(X_test, y_test))