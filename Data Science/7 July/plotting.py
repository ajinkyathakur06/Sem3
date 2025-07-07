import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV
df = pd.read_csv('Data Science/StudentsPerformance.csv')

# Add a new column: average score
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

#Pairplot for score relationships
sns.pairplot(df, vars=['math score', 'reading score', 'writing score'],hue='gender')
plt.title('Pairplot of Student Scores by Gender', y=1.02)

plt.figure(figsize=(10, 6))
plt.plot(df['average_score'], label='Average Score')
plt.title('Average Score of Students')

#display
plt.show()
