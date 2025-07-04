import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:\\Users\\malli\\Downloads\\bank+marketing\\bank-additional\\bank-additional\\bank-additional-full.csv", sep=';')

# Encode categorical variables using one-hot encoding
data_encoded = pd.get_dummies(data.drop('y', axis=1))
data_encoded['y'] = data['y'].map({'yes': 1, 'no': 0})

# Split dataset
X = data_encoded.drop('y', axis=1)
y = data_encoded['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Visualize
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=["No", "Yes"])
plt.show()
