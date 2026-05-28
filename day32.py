# =========================================
# AI/ML Internship – Day 32
# Seaborn Introduction & Statistical Visualization
# =========================================

import seaborn as sns
import matplotlib.pyplot as plt
import random

# =========================================
# Task 1: Theory Answers
# =========================================

print("1. What is Seaborn?")
print("Seaborn is a Python library used for advanced statistical visualization.")

print("\n2. Difference between Matplotlib and Seaborn")
print("Matplotlib is used for basic visualization.")
print("Seaborn is used for advanced and attractive visualization.")

print("\n3. Why Seaborn is important?")
print("Seaborn helps analyze datasets, visualize relationships, and detect patterns.")

print("\n4. What is statistical visualization?")
print("Statistical visualization is used for analyzing statistical patterns in data.")

print("\n5. What is box plot?")
print("Box plot helps identify outliers, data spread, and median values.")

# =========================================
# Task 2: Line Plot Practice
# =========================================

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

sns.set_style("darkgrid")

sns.lineplot(x=x, y=y)

plt.title("Simple Line Plot")

plt.show()

# Compare Data Trends
y2 = [15, 25, 35, 45]

sns.lineplot(x=x, y=y, label="Data 1")
sns.lineplot(x=x, y=y2, label="Data 2")

plt.title("Compare Data Trends")

plt.show()

# =========================================
# Task 3: Bar Plot Practice
# =========================================

# Student Marks Comparison
students = ["A", "B", "C"]
marks = [85, 90, 78]

sns.barplot(x=students, y=marks)

plt.title("Student Marks Comparison")

plt.show()

# Sales Comparison
products = ["Laptop", "Mobile", "Tablet"]
sales = [50, 80, 40]

sns.barplot(x=products, y=sales)

plt.title("Sales Comparison")

plt.show()

# Employee Salary Comparison
employees = ["Rahul", "Anu", "Meera"]
salary = [50000, 45000, 60000]

sns.barplot(x=employees, y=salary)

plt.title("Employee Salary Comparison")

plt.show()

# =========================================
# Task 4: Scatter Plot Practice
# =========================================

# Height vs Weight
height = [150, 160, 170, 180]
weight = [50, 60, 70, 80]

sns.scatterplot(x=height, y=weight)

plt.title("Height vs Weight")

plt.show()

# Study Hours vs Marks
study_hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 70, 90]

sns.scatterplot(x=study_hours, y=marks)

plt.title("Study Hours vs Marks")

plt.show()

# Temperature vs Sales
temperature = [20, 25, 30, 35]
sales = [100, 150, 200, 250]

sns.scatterplot(x=temperature, y=sales)

plt.title("Temperature vs Sales")

plt.show()

# =========================================
# Task 5: Histogram Practice
# =========================================

# Simple Histogram
data = [10, 20, 20, 30, 40, 40, 50]

sns.histplot(data)

plt.title("Histogram")

plt.show()

# Random Dataset Histogram
random_data = [random.randint(1, 100) for i in range(50)]

sns.histplot(random_data)

plt.title("Random Dataset Histogram")

plt.show()

# =========================================
# Task 6: Box Plot Practice
# =========================================

# Detect Outliers
data = [10, 20, 30, 40, 100]

sns.boxplot(x=data)

plt.title("Outlier Detection")

plt.show()

# Salary Dataset
salary_data = [25000, 30000, 35000, 40000, 100000]

sns.boxplot(x=salary_data)

plt.title("Salary Dataset Analysis")

plt.show()

# Marks Dataset
marks_data = [45, 50, 60, 70, 95]

sns.boxplot(x=marks_data)

plt.title("Marks Dataset Analysis")

plt.show()

# =========================================
# Task 7: Count Plot Practice
# =========================================

# Course Count
courses = ["AI", "Web", "AI", "Cloud", "AI"]

sns.countplot(x=courses)

plt.title("Course Count")

plt.show()

# Department Count
departments = ["HR", "AI", "HR", "Web", "AI"]

sns.countplot(x=departments)

plt.title("Department Count")

plt.show()

# Product Category Count
categories = ["Mobile", "Laptop", "Mobile", "Tablet", "Laptop"]

sns.countplot(x=categories)

plt.title("Product Category Count")

plt.show()

# =========================================
# End of Program
# =========================================