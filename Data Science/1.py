import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV
df = pd.read_csv('Data Science/StudentsPerformance.csv')

# Add a new column: average score
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Filter high achievers
high_achievers = df[df['average_score'] >= 80]

# print("High Achievers:")
# print(high_achievers)

# Heatmap of score correlations
plt.figure()
correlation_matrix = df[['math score', 'reading score', 'writing score']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Score Correlation Heatmap')

# Count plot: Students by gender
plt.figure()
sns.countplot(x='gender', data=df)
plt.title('Count of Students by Gender')

# Count plot of average scores by gender
plt.figure()
sns.countplot(x='average_score',hue='gender', data=df)
plt.title('Count of Average Scores by Gender')


# Show all plots at once and wait until user closes them
plt.show()

