import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\malli\\Downloads\\archive\\age_gender.csv")  # Replace with your actual file path

# Display the first few rows to understand the data structure
print(df.head())

# Set the Seaborn style for better aesthetics
sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='age', bins=20, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
