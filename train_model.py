import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load data
data = pd.read_csv("dataset.csv")

X = data[['Age', 'Income', 'CreditScore', 'ExistingLoans']]
y = data['LoanStatus']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("loan_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
