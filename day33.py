# ==========================================
# Day 33 Tasks - Correlation, Heatmaps & Pairplots
# ==========================================

# ------------------------------------------
# Task 1: Theory Answers
# ------------------------------------------

# 1. What is Correlation?
# Correlation measures the relationship between two variables.
# It shows how one variable changes when another variable changes.

# 2. Difference between Positive and Negative Correlation
# Positive Correlation:
# Both variables increase or decrease together.
# Example: Study Hours and Marks.

# Negative Correlation:
# One variable increases while the other decreases.
# Example: Exercise Hours and Weight.

# 3. What is Heatmap?
# A heatmap is a graphical representation of data using colors.
# It is commonly used to visualize correlation values.

# 4. What is Pairplot?
# Pairplot is a Seaborn visualization that shows relationships
# between multiple variables using scatter plots and distributions.

# 5. Why Correlation is Important in ML?
# - Helps identify relationships between features.
# - Improves feature selection.
# - Helps remove redundant variables.
# - Improves prediction accuracy and data analysis.


# ------------------------------------------
# Import Libraries
# ------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==========================================
# Task 2: Correlation Practice
# ==========================================

data = {
    "StudyHours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 70, 80],
    "SleepHours": [8, 7, 6, 5, 4]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nCorrelation Matrix:")
print(df.corr())

# Analysis:
# StudyHours and Marks have strong positive correlation.
# StudyHours and SleepHours have negative correlation.
# Marks and SleepHours also have negative correlation.


# ==========================================
# Task 3: Heatmap Practice
# ==========================================

plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Analysis:
# Values close to +1 indicate strong positive correlation.
# Values close to -1 indicate strong negative correlation.


# ==========================================
# Task 4: Pairplot Practice
# ==========================================

sns.pairplot(df)
plt.show()

# Analysis:
# Pairplot shows relationships among all variables.
# Scatter plots display correlations.
# Diagonal plots show distributions.


# ==========================================
# Task 5: Scatter Plot Practice
# ==========================================

# 1. Study Hours vs Marks

sns.scatterplot(x="StudyHours", y="Marks", data=df)
plt.title("Study Hours vs Marks")
plt.show()


# 2. Salary vs Experience

salary_data = {
    "Experience": [1, 2, 3, 4, 5, 6],
    "Salary": [25000, 30000, 35000, 45000, 55000, 65000]
}

salary_df = pd.DataFrame(salary_data)

sns.scatterplot(x="Experience", y="Salary", data=salary_df)
plt.title("Experience vs Salary")
plt.show()


# 3. Temperature vs Sales

temp_data = {
    "Temperature": [20, 25, 30, 35, 40],
    "Sales": [100, 150, 200, 280, 350]
}

temp_df = pd.DataFrame(temp_data)

sns.scatterplot(x="Temperature", y="Sales", data=temp_df)
plt.title("Temperature vs Sales")
plt.show()


# ==========================================
# Task 6: Dataset Analysis
# ==========================================

# 1. Student Dataset

student_data = {
    "StudyHours": [2, 4, 6, 8, 10],
    "Marks": [50, 60, 70, 85, 95],
    "Attendance": [70, 75, 80, 90, 95]
}

student_df = pd.DataFrame(student_data)

print("\nStudent Dataset Correlation:")
print(student_df.corr())

sns.heatmap(student_df.corr(), annot=True, cmap="YlGnBu")
plt.title("Student Dataset Heatmap")
plt.show()


# 2. Employee Dataset

employee_data = {
    "Experience": [1, 2, 3, 4, 5],
    "Salary": [25000, 32000, 40000, 50000, 65000],
    "Performance": [60, 70, 75, 85, 95]
}

employee_df = pd.DataFrame(employee_data)

print("\nEmployee Dataset Correlation:")
print(employee_df.corr())

sns.heatmap(employee_df.corr(), annot=True, cmap="YlOrRd")
plt.title("Employee Dataset Heatmap")
plt.show()


# 3. Hospital Dataset

hospital_data = {
    "Age": [20, 30, 40, 50, 60],
    "BloodPressure": [110, 120, 130, 140, 150],
    "RiskScore": [10, 20, 35, 50, 70]
}

hospital_df = pd.DataFrame(hospital_data)

print("\nHospital Dataset Correlation:")
print(hospital_df.corr())

sns.heatmap(hospital_df.corr(), annot=True, cmap="Reds")
plt.title("Hospital Dataset Heatmap")
plt.show()


print("\nDay 33 Tasks Completed Successfully!")