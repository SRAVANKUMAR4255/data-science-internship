import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("C:\\Users\\malli\\Downloads\\archive (1)\\Titanic.csv")

# Display basic info
print("Shape of dataset:", df.shape)
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop columns with too many missing values or irrelevant columns
df.drop(columns=['Cabin'], inplace=True)  # 'Cabin' has many missing values

# Fill missing values in 'Age' with median age
df['Age'].fillna(df['Age'].median(), inplace=True)

# Fill missing values in 'Embarked' with the most common port (mode)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# Verify missing values handled
print("\nMissing Values after handling:")
print(df.isnull().sum())

# Basic statistics
print("\nBasic statistics for Age:")
print(df['Age'].describe())

# Plot histogram for Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=30, kde=True, color='blue')
plt.title('Age Distribution of Titanic Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Optional: Plot countplot for 'Sex' to show gender distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='Sex', data=df)
plt.title('Gender Distribution on Titanic')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()
