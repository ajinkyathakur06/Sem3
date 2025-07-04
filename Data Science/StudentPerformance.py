import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import webbrowser
import base64
from io import BytesIO

# Read the CSV
df = pd.read_csv('Data Science/StudentsPerformance.csv')

# Add a new column: average score
df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

# Filter high achievers
high_achievers = df[df['average_score'] >= 80]

# Convert DataFrame to HTML
html_table = high_achievers.to_html(classes='table table-bordered', index=False)

# Create plot
gender_groups = df.groupby('gender')['average_score'].mean()
plt.figure(figsize=(6, 4))
gender_groups.plot(kind='bar', color=['blue', 'pink'])
plt.title('Average Score by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')
plt.xticks(rotation=0)

# Save plot to memory buffer
buf = BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
plt.close()
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode('utf-8')
buf.close()

# HTML content
html_content = f"""
<html>
<head>
    <title>High Achievers Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; padding: 20px; }}
        .table {{ border-collapse: collapse; width: 100%; }}
        .table th, .table td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        .table th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>High Achievers</h1>
    {html_table}
    <h2>Average Score by Gender</h2>
    <img src="data:image/png;base64,{img_base64}" alt="Bar chart">
</body>
</html>
"""

# Save and open in browser
file_path = "report.html"
with open(file_path, "w") as f:
    f.write(html_content)

webbrowser.open(file_path)
