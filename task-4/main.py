import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load only the first 100,000 rows to avoid memory issues
df = pd.read_csv("C:\\Users\\malli\\Downloads\\archive (2)\\US_Accidents_March23.csv", nrows=100000)

# Convert time columns to datetime
df['Start_Time'] = pd.to_datetime(df['Start_Time'])
df['End_Time'] = pd.to_datetime(df['End_Time'])

# Extract time-based features
df['Hour'] = df['Start_Time'].dt.hour
df['Weekday'] = df['Start_Time'].dt.day_name()
df['Month'] = df['Start_Time'].dt.month_name()

# ---------- Time of Day Analysis ----------
plt.figure(figsize=(12, 6))
sns.countplot(x='Hour', data=df, hue='Hour', palette='coolwarm', legend=False)
plt.title('Accidents by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Weekday Analysis ----------
plt.figure(figsize=(12, 6))
sns.countplot(x='Weekday', data=df, order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
], hue='Weekday', palette='viridis', legend=False)
plt.title('Accidents by Day of the Week')
plt.xlabel('Day')
plt.ylabel('Accidents Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Weather Condition Analysis ----------
top_weather = df['Weather_Condition'].value_counts().nlargest(10).index
plt.figure(figsize=(12, 6))
sns.countplot(data=df[df['Weather_Condition'].isin(top_weather)],
              y='Weather_Condition', order=top_weather, hue='Weather_Condition', palette='Set2', legend=False)
plt.title('Top 10 Weather Conditions during Accidents')
plt.xlabel('Count')
plt.ylabel('Weather Condition')
plt.tight_layout()
plt.show()

# ---------- Road Conditions ----------
road_features = ['Amenity', 'Bump', 'Crossing', 'Junction', 'Traffic_Signal']
road_conditions = df[road_features].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=road_conditions.index, y=road_conditions.values, palette='flare')
plt.title('Accidents at Different Road Features')
plt.ylabel('Number of Accidents')
plt.tight_layout()
plt.show()

# ---------- Severity vs Weather ----------
plt.figure(figsize=(10, 6))
sns.boxplot(x='Severity', y='Temperature(F)', data=df)
plt.title('Severity vs Temperature')
plt.tight_layout()
plt.show()

