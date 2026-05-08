# ==============================
# AI/ML Internship - Day 17
# Error-Free Code
# ==============================

# ------------------------------
# Part 1: Math Module
# ------------------------------

import math

# 1. Find square root
print("Square Root:", math.sqrt(16))

# 2. Find power
print("Power:", math.pow(2, 3))

# 3. Round numbers
print("Ceil:", math.ceil(2.3))
print("Floor:", math.floor(2.9))

# 4. Use pi value
print("PI Value:", math.pi)

print("\n")


# ------------------------------
# Part 2: Random Module
# ------------------------------

import random

# 1. Generate random number
print("Random Number:", random.randint(1, 10))

# 2. Pick random element
print("Random Choice:", random.choice([10, 20, 30]))

# 3. Generate list of random numbers
numbers = []

for i in range(5):
    numbers.append(random.randint(1, 100))

print("Random List:", numbers)

print("\n")


# ------------------------------
# Part 3: Datetime Module
# ------------------------------

import datetime

# Current date and time
now = datetime.datetime.now()

# 1. Print current date
print("Current Date:", now)

# 2. Format date
print("Formatted Date:", now.strftime("%Y-%m-%d"))

# 3. Extract year and month
print("Year:", now.year)
print("Month:", now.month)

print("\n")


# ------------------------------
# Part 4: Line Graph
# ------------------------------

import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [10, 20, 30]

plt.figure()
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()


# ------------------------------
# Part 5: Bar Chart
# ------------------------------

plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()


# ------------------------------
# Part 6: Student Marks Graph
# ------------------------------

students = ["A", "B", "C"]
marks = [85, 90, 78]

plt.figure()
plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()