# ==========================================
# AI/ML Internship – Day 40 Tasks
# Module 7: Decision Tree Classification
# ==========================================

# ==========================================
# Task 1: Theory Answers
# ==========================================

print("TASK 1: THEORY ANSWERS\n")

print("1. What is a Decision Tree?")
print("A Decision Tree is a supervised machine learning algorithm that makes predictions using decision rules and tree-like structures.\n")

print("2. What is a Root Node?")
print("The Root Node is the first question or decision point in a decision tree.\n")

print("3. What is a Branch?")
print("A Branch is a path that connects one decision node to another node.\n")

print("4. What is a Leaf Node?")
print("A Leaf Node is the final output or prediction of the decision tree.\n")

print("5. Advantages of Decision Trees?")
print("- Easy to understand")
print("- Easy to visualize")
print("- Works for classification and regression")
print("- Requires less data preparation")
print("- No complex mathematics\n")


# ==========================================
# Task 2: Dataset Creation
# ==========================================

import pandas as pd

print("TASK 2: DATASET CREATION\n")

# Student Result Dataset
student_data = {
    "Hours": [1, 2, 3, 5, 6, 7],
    "Result": [0, 0, 0, 1, 1, 1]
}

student_df = pd.DataFrame(student_data)

print("Student Dataset")
print(student_df)
print()

# Loan Approval Dataset
loan_data = {
    "Income": [20000, 25000, 30000, 50000, 60000, 70000],
    "Loan_Status": [0, 0, 0, 1, 1, 1]
}

loan_df = pd.DataFrame(loan_data)

print("Loan Approval Dataset")
print(loan_df)
print()

# Disease Prediction Dataset
disease_data = {
    "Temperature": [98, 99, 100, 101, 102, 103],
    "Disease": [0, 0, 0, 1, 1, 1]
}

disease_df = pd.DataFrame(disease_data)

print("Disease Dataset")
print(disease_df)
print()


# ==========================================
# Task 3: Model Building
# ==========================================

from sklearn.tree import DecisionTreeClassifier

print("TASK 3: MODEL BUILDING\n")

# Student Model
X_student = student_df[["Hours"]]
y_student = student_df["Result"]

student_model = DecisionTreeClassifier()
student_model.fit(X_student, y_student)

print("Student Model Trained Successfully")
print()


# ==========================================
# Task 4: Prediction Practice
# ==========================================

print("TASK 4: PREDICTIONS\n")

# Student Result Prediction
student_prediction = student_model.predict([[5]])
print("Student Result Prediction:", student_prediction)

# Disease Prediction Model
X_disease = disease_df[["Temperature"]]
y_disease = disease_df["Disease"]

disease_model = DecisionTreeClassifier()
disease_model.fit(X_disease, y_disease)

disease_prediction = disease_model.predict([[102]])
print("Disease Prediction:", disease_prediction)

# Loan Prediction Model
X_loan = loan_df[["Income"]]
y_loan = loan_df["Loan_Status"]

loan_model = DecisionTreeClassifier()
loan_model.fit(X_loan, y_loan)

loan_prediction = loan_model.predict([[55000]])
print("Loan Approval Prediction:", loan_prediction)

print()


# ==========================================
# Task 5: Tree Analysis
# ==========================================

print("TASK 5: TREE ANALYSIS\n")

print("Root Node:")
print("Study Hours > 4\n")

print("Leaf Nodes:")
print("Pass")
print("Fail\n")

print("Decision Path:")
print("If Study Hours > 4 -> Pass")
print("If Study Hours <= 4 -> Fail\n")


# ==========================================
# Task 6: Compare Algorithms
# ==========================================

print("TASK 6: ALGORITHM COMPARISON\n")

comparison = pd.DataFrame({
    "Feature": [
        "Working Method",
        "Prediction Speed",
        "Interpretability",
        "Visualization",
        "Best For"
    ],
    "Logistic Regression": [
        "Probability Based",
        "Fast",
        "Medium",
        "No",
        "Linear Classification"
    ],
    "KNN": [
        "Nearest Neighbors",
        "Slow",
        "Low",
        "No",
        "Similarity-Based Problems"
    ],
    "Decision Tree": [
        "Decision Rules",
        "Fast",
        "High",
        "Yes",
        "Rule-Based Decisions"
    ]
})

print(comparison)

print("\nDay 40 Tasks Completed Successfully!")