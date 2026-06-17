# ==========================================
# AI/ML Internship – Day 39
# Module 7: K-Nearest Neighbors (KNN)
# ==========================================

# ==========================================
# Task 1: Theory Answers
# ==========================================

# 1. What is KNN?
# KNN (K-Nearest Neighbors) is a supervised machine learning algorithm
# used for classification and regression. It predicts results based on
# the nearest data points.

# 2. What does K mean in KNN?
# K represents the number of nearest neighbors considered for prediction.
# Example: K = 3 means the algorithm checks the 3 nearest data points.

# 3. Is KNN supervised or unsupervised?
# KNN is a Supervised Learning algorithm.

# 4. What is a neighbor?
# A neighbor is a nearby data point used by KNN to make predictions.

# 5. Advantages of KNN?
# - Easy to understand
# - Easy to implement
# - No complex training required
# - Works well on small datasets


# ==========================================
# Task 2: Dataset Practice
# ==========================================

import pandas as pd

# Student Result Dataset
student_data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}
student_df = pd.DataFrame(student_data)
print("Student Dataset")
print(student_df)

# Disease Dataset
disease_data = {
    "Age": [20, 25, 30, 40, 50, 60],
    "Disease": [0, 0, 0, 1, 1, 1]
}
disease_df = pd.DataFrame(disease_data)
print("\nDisease Dataset")
print(disease_df)

# Loan Approval Dataset
loan_data = {
    "Income": [20000, 25000, 30000, 50000, 60000, 70000],
    "Loan_Status": [0, 0, 0, 1, 1, 1]
}
loan_df = pd.DataFrame(loan_data)
print("\nLoan Approval Dataset")
print(loan_df)


# ==========================================
# Task 3: KNN Model
# ==========================================

from sklearn.neighbors import KNeighborsClassifier

X = student_df[["Hours"]]
y = student_df["Result"]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X, y)

prediction = model.predict([[4]])

print("\nPrediction for 4 Hours:")
print(prediction)

if prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")


# ==========================================
# Task 4: Experiment with K Values
# ==========================================

print("\nComparing Different K Values")

for k in [1, 3, 5]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X, y)

    prediction = model.predict([[4]])

    print(f"K = {k} --> Prediction = {prediction[0]}")


# ==========================================
# Task 5: Classification Practice
# ==========================================

# 1. Student Result Prediction

student_model = KNeighborsClassifier(n_neighbors=3)
student_model.fit(student_df[["Hours"]], student_df["Result"])

student_prediction = student_model.predict([[4]])
print("\nStudent Result Prediction:", student_prediction)

# 2. Disease Status Prediction

disease_model = KNeighborsClassifier(n_neighbors=3)
disease_model.fit(disease_df[["Age"]], disease_df["Disease"])

disease_prediction = disease_model.predict([[45]])
print("Disease Status Prediction:", disease_prediction)

# 3. Customer Category Prediction

customer_data = {
    "Purchase": [1000, 1500, 2000, 5000, 6000, 7000],
    "Category": [0, 0, 0, 1, 1, 1]
}

customer_df = pd.DataFrame(customer_data)

customer_model = KNeighborsClassifier(n_neighbors=3)
customer_model.fit(customer_df[["Purchase"]], customer_df["Category"])

customer_prediction = customer_model.predict([[5500]])
print("Customer Category Prediction:", customer_prediction)


# ==========================================
# Task 6: Comparison Activity
# ==========================================

print("\nDifference Between Logistic Regression and KNN")

comparison = """
Logistic Regression:
1. Learns a mathematical relationship.
2. Fast prediction.
3. Model-based algorithm.
4. Works well on large datasets.

KNN:
1. Uses nearest neighbors for prediction.
2. Slower prediction.
3. Instance-based algorithm.
4. Better for small datasets.
"""

print(comparison)