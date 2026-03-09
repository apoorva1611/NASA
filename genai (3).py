# Simple Blood Pressure Prediction System

from sklearn.tree import DecisionTreeClassifier

# Sample data
age = [25, 30, 45, 50, 35]
heart_rate = [72, 75, 80, 85, 70]
weight = [60, 65, 75, 80, 68]

# BP result (0 = Normal, 1 = High)
bp = [0, 0, 1, 1, 0]

# Combine inputs
X = list(zip(age, heart_rate, weight))
y = bp

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# User input
a = int(input("Enter Age: "))
h = int(input("Enter Heart Rate: "))
w = int(input("Enter Weight: "))

# Prediction
result = model.predict([[a, h, w]])

# Output
if result[0] == 0:
    print("Blood Pressure: Normal")
else:
    print("Blood Pressure: High")