# ==========================================
# AI/ML Internship – Day 41
# Module 7: Random Forest Classification
# ==========================================

# ==========================================
# Task 1: Theory Answers
# ==========================================

print("\n===== TASK 1: THEORY ANSWERS =====\n")

print("1. What is Random Forest?")
print("Random Forest is a supervised machine learning algorithm that combines multiple Decision Trees to improve prediction accuracy.\n")

print("2. What is an Ensemble Method?")
print("An Ensemble Method combines multiple machine learning models to make better predictions.\n")

print("3. What is Voting?")
print("Each Decision Tree gives a prediction, and the majority prediction becomes the final output.\n")

print("4. Advantages of Random Forest")
print("- High Accuracy")
print("- Reduces Overfitting")
print("- Handles Large Datasets")
print("- Reliable Predictions")
print("- Works for Classification and Regression\n")

print("5. Difference Between Decision Tree and Random Forest")
print("""
Decision Tree            Random Forest
------------------------------------------------
Single Tree              Multiple Trees
Can Overfit              Less Overfitting
Faster                   Slightly Slower
Less Accurate            More Accurate
Easy to Visualize        Harder to Visualize
""")

# ==========================================
# Import Libraries
# ==========================================

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# ==========================================
# Task 2 & Task 3
# Student Result Dataset
# ==========================================

print("\n===== STUDENT RESULT DATASET =====\n")

student_data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

student_df = pd.DataFrame(student_data)

print(student_df)

X_student = student_df[["Hours"]]
y_student = student_df["Result"]

student_model = RandomForestClassifier(n_estimators=100)
student_model.fit(X_student, y_student)

student_prediction = student_model.predict([[4]])

print("\nPrediction for 4 Study Hours:")

if student_prediction[0] == 1:
    print("PASS")
else:
    print("FAIL")

# ==========================================
# Disease Dataset
# ==========================================

print("\n===== DISEASE DATASET =====\n")

disease_data = {
    "Fever": [1, 1, 0, 0, 1, 0],
    "Disease": [1, 1, 0, 0, 1, 0]
}

disease_df = pd.DataFrame(disease_data)

print(disease_df)

X_disease = disease_df[["Fever"]]
y_disease = disease_df["Disease"]

disease_model = RandomForestClassifier(n_estimators=100)
disease_model.fit(X_disease, y_disease)

disease_prediction = disease_model.predict([[1]])

print("\nPrediction:")

if disease_prediction[0] == 1:
    print("Disease Detected")
else:
    print("No Disease")

# ==========================================
# Loan Approval Dataset
# ==========================================

print("\n===== LOAN APPROVAL DATASET =====\n")

loan_data = {
    "Income": [20000, 30000, 40000, 50000, 60000, 70000],
    "Loan": [0, 0, 0, 1, 1, 1]
}

loan_df = pd.DataFrame(loan_data)

print(loan_df)

X_loan = loan_df[["Income"]]
y_loan = loan_df["Loan"]

loan_model = RandomForestClassifier(n_estimators=100)
loan_model.fit(X_loan, y_loan)

loan_prediction = loan_model.predict([[55000]])

print("\nPrediction:")

if loan_prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")

# ==========================================
# Task 4: Prediction Practice
# ==========================================

print("\n===== TASK 4: PREDICTION PRACTICE =====\n")

student_result = student_model.predict([[5]])
print("Student Result Prediction:", student_result)

disease_result = disease_model.predict([[1]])
print("Disease Status Prediction:", disease_result)

loan_result = loan_model.predict([[55000]])
print("Loan Approval Prediction:", loan_result)

# ==========================================
# Task 5: Parameter Practice
# ==========================================

print("\n===== TASK 5: PARAMETER PRACTICE =====\n")

for trees in [10, 50, 100]:
    model = RandomForestClassifier(n_estimators=trees)
    model.fit(X_student, y_student)

    prediction = model.predict([[4]])

    print("Number of Trees:", trees)
    print("Prediction:", prediction)
    print()

# ==========================================
# Task 6: Compare Algorithms
# ==========================================

print("\n===== TASK 6: COMPARISON =====\n")

print("""
Feature          Decision Tree      Random Forest      KNN
--------------------------------------------------------------
Type             Supervised         Supervised         Supervised
Model            Single Tree        Multiple Trees     Distance Based
Accuracy         Medium             High               Medium-High
Overfitting      High               Low                Low
Speed            Fast               Moderate           Slow
Complexity       Simple             Moderate           Simple
Best Use         Small Data         Large Data         Similar Data
""")

print("Conclusion:")
print("1. Decision Tree is simple and fast.")
print("2. Random Forest is more accurate and reliable.")
print("3. KNN predicts using nearest neighbors.")
print("4. Random Forest reduces overfitting and gives better performance.")