# =========================================
# AI/ML Internship – Day 30
# Data Visualization Basics with Matplotlib
# =========================================

import matplotlib.pyplot as plt

# =========================================
# Task 1: Theory Answers
# =========================================

print("1. What is Matplotlib?")
print("Matplotlib is a Python library used for creating graphs and charts.")

print("\n2. Why visualization is important?")
print("Visualization helps understand data, analyze patterns, and improve decision making.")

print("\n3. What is plot?")
print("A plot is a graphical representation of data.")

print("\n4. Difference between X-axis and Y-axis")
print("X-axis is horizontal axis.")
print("Y-axis is vertical axis.")

print("\n5. Why graphs are important in AI?")
print("Graphs help visualize trends, predictions, accuracy, and model performance.")

# =========================================
# Task 2: Line Plot Practice
# =========================================

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()

# =========================================
# Task 3: Styling Graphs
# =========================================

x = [1, 2, 3, 4]
y = [15, 25, 35, 45]

plt.plot(x, y, linestyle="--", marker="o", label="Marks")

plt.title("Styled Line Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.legend()
plt.grid()

plt.show()

# =========================================
# Task 4: Bar Chart Practice
# =========================================

# Student Marks Comparison
students = ["A", "B", "C"]
marks = [80, 90, 75]

plt.bar(students, marks)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# Sales Comparison
products = ["Laptop", "Mobile", "Tablet"]
sales = [50, 80, 40]

plt.bar(products, sales)

plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# Product Comparison
items = ["AI", "Web", "Cloud"]
values = [70, 60, 50]

plt.bar(items, values)

plt.title("Product Comparison")
plt.xlabel("Category")
plt.ylabel("Values")

plt.show()

# =========================================
# Task 5: Pie Chart Practice
# =========================================

# Department Distribution
data = [40, 30, 20, 10]
labels = ["AI", "Web", "Cloud", "Cyber"]

plt.pie(data, labels=labels)

plt.title("Department Distribution")

plt.show()

# Expense Analysis
expenses = [5000, 3000, 2000]
labels = ["Food", "Travel", "Shopping"]

plt.pie(expenses, labels=labels)

plt.title("Expense Analysis")

plt.show()

# Course Popularity
courses = [45, 35, 20]
labels = ["Python", "AI", "Data Science"]

plt.pie(courses, labels=labels)

plt.title("Course Popularity")

plt.show()

# =========================================
# Task 6: Scatter Plot Practice
# =========================================

# Height vs Weight
height = [150, 160, 170, 180]
weight = [50, 60, 70, 80]

plt.scatter(height, weight)

plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")

plt.show()

# Study Hours vs Marks
study_hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 70, 90]

plt.scatter(study_hours, marks)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# Temperature vs Sales
temperature = [20, 25, 30, 35]
sales = [100, 150, 200, 250]

plt.scatter(temperature, sales)

plt.title("Temperature vs Sales")
plt.xlabel("Temperature")
plt.ylabel("Sales")

plt.show()

# =========================================
# End of Program
# =========================================