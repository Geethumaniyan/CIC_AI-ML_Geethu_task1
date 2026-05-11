# ============================================
# AI/ML Internship – Day 19
# Module 4: NumPy Operations – Part 2
# ============================================

# ============================================
# Import NumPy
# ============================================

import numpy as np


# ============================================
# Task 1: Theory
# ============================================

print("========== TASK 1: THEORY ==========\n")

# 1. What is vectorization?
print("1. What is Vectorization?")
print("Vectorization means performing operations on entire arrays without loops.\n")

# Example
arr = np.array([1, 2, 3])

print("Vectorization Example:")
print(arr * 2)
print()


# 2. Difference between list and NumPy operations
print("2. Difference between List and NumPy Operations")

# Python List
a = [1,2,3]
b = [4,5,6]

print("Python List Addition:")
print(a + b)

# NumPy Array
a1 = np.array([1,2,3])
b1 = np.array([4,5,6])

print("NumPy Array Addition:")
print(a1 + b1)
print()


# 3. What are aggregation functions?
print("3. What are Aggregation Functions?")
print("Aggregation functions are used to calculate summary statistics like sum, mean, max, and min.\n")


# 4. What is axis?
print("4. What is Axis?")
print("Axis is used in multi-dimensional arrays.")
print("axis=0 → column-wise")
print("axis=1 → row-wise\n")


# 5. Why NumPy is faster?
print("5. Why NumPy is Faster?")
print("NumPy is faster because it is optimized in C and supports vectorized operations.\n")


# ============================================
# Task 2: Arithmetic Practice
# ============================================

print("========== TASK 2: ARITHMETIC PRACTICE ==========\n")

a = np.array([1,2,3])
b = np.array([4,5,6])

# Addition
print("Addition:")
print(a + b)
print()

# Multiplication
print("Multiplication:")
print(a * b)
print()

# Division
print("Division:")
print(a / b)
print()


# ============================================
# Task 3: Scalar Operations
# ============================================

print("========== TASK 3: SCALAR OPERATIONS ==========\n")

arr = np.array([1,2,3])

# Add constant
print("Add Constant:")
print(arr + 10)
print()

# Multiply array
print("Multiply Array:")
print(arr * 2)
print()

# Subtract constant
print("Subtract Constant:")
print(arr - 1)
print()


# ============================================
# Task 4: Math Functions
# ============================================

print("========== TASK 4: MATH FUNCTIONS ==========\n")

arr = np.array([1,4,9])

# Square Root
print("Square Root:")
print(np.sqrt(arr))
print()

# Log Values
print("Log Values:")
print(np.log(arr))
print()

# Exponential Values
print("Exponential Values:")
print(np.exp(arr))
print()


# Rounding Functions
arr2 = np.array([1.2, 2.7, 3.5])

print("Round Values:")
print(np.round(arr2))
print()

print("Ceil Values:")
print(np.ceil(arr2))
print()

print("Floor Values:")
print(np.floor(arr2))
print()


# ============================================
# Task 5: Aggregation
# ============================================

print("========== TASK 5: AGGREGATION ==========\n")

arr = np.array([10,20,30,40])

# Sum
print("Sum:")
print(np.sum(arr))
print()

# Mean
print("Mean:")
print(np.mean(arr))
print()

# Max
print("Maximum:")
print(np.max(arr))
print()

# Min
print("Minimum:")
print(np.min(arr))
print()


# ============================================
# Task 6: Axis Practice
# ============================================

print("========== TASK 6: AXIS PRACTICE ==========\n")

arr = np.array([[1,2],
                [3,4]])

# Column-wise Sum
print("Column-wise Sum (axis=0):")
print(np.sum(arr, axis=0))
print()

# Row-wise Sum
print("Row-wise Sum (axis=1):")
print(np.sum(arr, axis=1))
print()


# ============================================
# Task 7: Filtering
# ============================================

print("========== TASK 7: FILTERING ==========\n")

arr = np.array([10,20,30,40,50])

# Filter values > 20
print("Values Greater Than 20:")
print(arr[arr > 20])
print()

# Filter even numbers
print("Even Numbers:")
print(arr[arr % 2 == 0])
print()


# ============================================
# End of Program
# ============================================

print("========== ALL TASKS COMPLETED ==========")