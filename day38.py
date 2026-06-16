# ==========================================
# AI/ML Internship – Day 38 Tasks
# Module 7: Logistic Regression
# ==========================================

# ==========================================
# Task 1: Theory Answers
# ==========================================

print("TASK 1: THEORY ANSWERS\n")

print("1. What is Logistic Regression?")
print("Logistic Regression is a supervised machine learning algorithm used for classification tasks.\n")

print("2. Why is it used?")
print("It is used when the output is a category such as Pass/Fail, Spam/Not Spam, or Disease/No Disease.\n")

print("3. What is Binary Classification?")
print("Binary Classification is a classification problem with only two possible classes.")
print("Examples: Yes/No, True/False, Spam/Not Spam.\n")

print("4. What is a Class Label?")
print("A class label is the output category predicted by the model.\n")

print("5. Difference between Linear and Logistic Regression?")
print("Linear Regression predicts numerical values.")
print("Logistic Regression predicts categorical values.\n")


# ==========================================
# Task 2: Dataset Creation
# ==========================================

import pandas as pd

print("TASK 2: DATASET CREATION\n")

# Pass/Fail Dataset
pass_fail = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5, 6],
    "Result": [0, 0, 0, 1, 1, 1]
})

print("Pass/Fail Dataset")
print(pass_fail)
print()

# Disease Dataset
disease = pd.DataFrame({
    "Age": [20, 25, 30, 45, 50, 60],
    "Disease": [0, 0, 0, 1, 1, 1]
})

print("Disease Dataset")
print(disease)
print()

# Spam Dataset
spam = pd.DataFrame({
    "Message_Length": [10, 20, 30, 80, 90, 100],
    "Spam": [0, 0, 0, 1, 1, 1]
})

print("Spam Dataset")
print(spam)
print()


# ==========================================
# Task 3: Model Training
# ==========================================

from sklearn.linear_model import LogisticRegression

print("TASK 3: MODEL TRAINING\n")

X = pass_fail[["Hours"]]
y = pass_fail["Result"]

model = LogisticRegression()

model.fit(X, y)

print("Logistic Regression Model Trained Successfully\n")


# ==========================================
# Task 4: Prediction Practice
# ==========================================

print("TASK 4: PREDICTION PRACTICE\n")

# Student Result Prediction
student_prediction = model.predict([[5]])
print("Student Prediction (5 Hours):", student_prediction)

# Disease Prediction
X_disease = disease[["Age"]]
y_disease = disease["Disease"]

disease_model = LogisticRegression()
disease_model.fit(X_disease, y_disease)

disease_prediction = disease_model.predict([[55]])
print("Disease Prediction (Age 55):", disease_prediction)

# Spam Prediction
X_spam = spam[["Message_Length"]]
y_spam = spam["Spam"]

spam_model = LogisticRegression()
spam_model.fit(X_spam, y_spam)

spam_prediction = spam_model.predict([[95]])
print("Spam Prediction (Length 95):", spam_prediction)
print()


# ==========================================
# Task 5: Probability Analysis
# ==========================================

print("TASK 5: PROBABILITY ANALYSIS\n")

probability = model.predict_proba([[5]])

print("Probability Output:")
print(probability)
print()

print("Explanation:")
print("First Value  -> Probability of Fail")
print("Second Value -> Probability of Pass")
print("Higher probability indicates higher confidence.\n")


# ==========================================
# Task 6: Classification Logic
# ==========================================

print("TASK 6: CLASSIFICATION LOGIC\n")

print("1. Pass/Fail Prediction       -> Yes")
print("2. House Price Prediction     -> No")
print("3. Spam Detection             -> Yes")
print("4. Disease Prediction         -> Yes")
print("5. Salary Prediction          -> No")