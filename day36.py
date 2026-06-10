# ==========================================
# AI/ML Internship – Day 36
# Module 7: Train-Test Split & Model Evaluation
# ==========================================

# ==========================================
# Task 1: Theory Answers
# ==========================================

print("TASK 1: THEORY ANSWERS\n")

print("1. What is Train Data?")
print("Train data is the portion of the dataset used to train the machine learning model.\n")

print("2. What is Test Data?")
print("Test data is the portion of the dataset used to evaluate the model's performance.\n")

print("3. What is Train-Test Split?")
print("Train-test split is the process of dividing a dataset into training and testing datasets.\n")

print("4. Why is Model Evaluation Important?")
print("Model evaluation helps measure the accuracy, performance, and prediction quality of a machine learning model.\n")

print("5. What is Accuracy?")
print("Accuracy shows how correctly the model makes predictions compared to actual values.\n")


# ==========================================
# Import Libraries
# ==========================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# ==========================================
# Task 2: Dataset Practice
# ==========================================

print("\nTASK 2: DATASET PRACTICE\n")

# Student Dataset
student_data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}

student_df = pd.DataFrame(student_data)
print("Student Dataset:")
print(student_df)

# Salary Dataset
salary_data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [25000, 30000, 35000, 45000, 50000, 60000, 70000, 80000]
}

salary_df = pd.DataFrame(salary_data)
print("\nSalary Dataset:")
print(salary_df)

# Sales Dataset
sales_data = {
    "Advertising": [10, 20, 30, 40, 50, 60, 70, 80],
    "Sales": [100, 150, 200, 250, 300, 350, 400, 450]
}

sales_df = pd.DataFrame(sales_data)
print("\nSales Dataset:")
print(sales_df)


# ==========================================
# Task 3: Train-Test Split Practice
# ==========================================

X = student_df[["Hours"]]
y = student_df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTASK 3: TRAIN-TEST SPLIT")
print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


# ==========================================
# Task 4: Model Training
# ==========================================

model = LinearRegression()

# Train with training data only
model.fit(X_train, y_train)

print("\nTASK 4: MODEL TRAINING COMPLETED")


# ==========================================
# Task 5: Prediction Practice
# ==========================================

predictions = model.predict(X_test)

print("\nTASK 5: PREDICTIONS")
print(predictions)

result = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nActual vs Predicted")
print(result)

score = model.score(X_test, y_test)

print("\nAccuracy Score:", score)


# ==========================================
# Task 6: Result Analysis
# ==========================================

print("\nTASK 6: RESULT ANALYSIS\n")

print("1. Good Predictions:")
print("Predicted values are close to actual values.\n")

print("2. Prediction Errors:")
print("Difference between actual values and predicted values.\n")

print("3. Accuracy Meaning:")
print("A higher accuracy score indicates better model performance and prediction quality.")