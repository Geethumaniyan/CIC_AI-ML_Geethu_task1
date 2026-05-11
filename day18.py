# ============================================
# AI/ML Internship – Day 18
# Module 4: NumPy Fundamentals – Part 1
# ============================================

# ============================================
# Import NumPy
# ============================================

import numpy as np


# ============================================
# Task 1: Theory
# ============================================

print("========== TASK 1: THEORY ==========\n")

# 1. What is NumPy?
print("1. What is NumPy?")
print("NumPy is a Python library used for numerical computations, arrays, and fast data processing.\n")

# Example
arr = np.array([1, 2, 3])
print("Example Array:")
print(arr)
print()


# 2. Why NumPy is faster than lists?
print("2. Why NumPy is faster than lists?")
print("NumPy is faster because it is optimized in C and supports vector operations.\n")

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Addition using NumPy:")
print(a + b)
print()


# 3. What is Array?
print("3. What is Array?")
print("An array is a collection of similar data stored together.\n")

arr = np.array([10,20,30])

print("Array Example:")
print(arr)
print()


# 4. What is Shape and Dimension?
print("4. What is Shape and Dimension?")
print("Shape = rows and columns")
print("Dimension = number of axes\n")

arr = np.array([[1,2],[3,4]])

print("Shape:")
print(arr.shape)

print("Dimensions:")
print(arr.ndim)
print()


# 5. What is Reshaping?
print("5. What is Reshaping?")
print("Reshaping means changing array shape without changing data.\n")

arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2,3)

print("Reshaped Array:")
print(new_arr)
print()


# ============================================
# Task 2: Array Creation
# ============================================

print("========== TASK 2: ARRAY CREATION ==========\n")

# 1D Array
print("1D Array")

arr1 = np.array([1,2,3,4])

print(arr1)
print()


# 2D Array
print("2D Array")

arr2 = np.array([[1,2],[3,4]])

print(arr2)
print()


# 3D Array
print("3D Array")

arr3 = np.array([[[1,2],[3,4]]])

print(arr3)
print()


# ============================================
# Task 3: Properties
# ============================================

print("========== TASK 3: PROPERTIES ==========\n")

# Shape
print("Shape of arr2:")
print(arr2.shape)
print()

# Dimensions
print("Dimensions of arr2:")
print(arr2.ndim)
print()

# Data Type
print("Data Type of arr2:")
print(arr2.dtype)
print()


# ============================================
# Task 4: Special Arrays
# ============================================

print("========== TASK 4: SPECIAL ARRAYS ==========\n")

# Zero Matrix
print("Zero Matrix")

zeros_array = np.zeros((2,3))

print(zeros_array)
print()


# Ones Matrix
print("Ones Matrix")

ones_array = np.ones((2,2))

print(ones_array)
print()


# Identity Matrix
print("Identity Matrix")

identity_array = np.eye(3)

print(identity_array)
print()


# Range Array
print("Range Array")

range_array = np.arange(1,10)

print(range_array)
print()


# ============================================
# Task 5: Indexing & Slicing
# ============================================

print("========== TASK 5: INDEXING ==========\n")

arr = np.array([10,20,30,40])

# Access First Element
print("First Element:")
print(arr[0])
print()


# Slice Array
print("Slice Array:")
print(arr[1:3])
print()


# Access Element in 2D
print("Access Element in 2D Array")

arr2 = np.array([[1,2],[3,4]])

print(arr2[0,1])
print()


# ============================================
# Task 6: Reshaping
# ============================================

print("========== TASK 6: RESHAPING ==========\n")

# Convert 1D → 2D
print("Convert 1D to 2D")

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape(2,3)

print(reshaped)
print()


# Convert 2D → 1D
print("Convert 2D to 1D")

arr2 = np.array([[1,2,3],[4,5,6]])

flat = arr2.reshape(6)

print(flat)
print()


# ============================================
# End of Program
# ============================================

print("========== ALL TASKS COMPLETED ==========")