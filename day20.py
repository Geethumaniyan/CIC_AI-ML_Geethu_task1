# ============================================
# AI/ML Internship – Day 20
# Module 4: NumPy Indexing & Slicing – Deep Dive
# ============================================

# ============================================
# Import NumPy
# ============================================

import numpy as np


# ============================================
# Task 1: Theory
# ============================================

print("========== TASK 1: THEORY ==========\n")

# 1. What is Indexing?
print("1. What is Indexing?")
print("Indexing means accessing a specific element from an array.\n")

# Example
arr = np.array([10, 20, 30, 40])

print("First Element:")
print(arr[0])
print()


# 2. What is Slicing?
print("2. What is Slicing?")
print("Slicing means extracting multiple elements from an array.\n")

print("Slice Example:")
print(arr[1:3])
print()


# 3. Difference between Indexing and Slicing
print("3. Difference between Indexing and Slicing")
print("Indexing returns a single value.")
print("Slicing returns multiple values.\n")


# 4. What is Boolean Indexing?
print("4. What is Boolean Indexing?")
print("Boolean indexing filters array values using conditions.\n")

print("Values Greater Than 20:")
print(arr[arr > 20])
print()


# 5. Why Indexing is Important in ML?
print("5. Why Indexing is Important in ML?")
print("Indexing helps select features, filter data, and extract image regions.\n")


# ============================================
# Task 2: 1D Practice
# ============================================

print("========== TASK 2: 1D PRACTICE ==========\n")

arr1 = np.array([10, 20, 30, 40])

# Access first element
print("First Element:")
print(arr1[0])
print()

# Access last element
print("Last Element:")
print(arr1[-1])
print()

# Slice array
print("Slice Array:")
print(arr1[1:3])
print()


# ============================================
# Task 3: 2D Practice
# ============================================

print("========== TASK 3: 2D PRACTICE ==========\n")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Access element
print("Access Element arr2[0,1]:")
print(arr2[0,1])
print()

# Print row
print("First Row:")
print(arr2[0])
print()

# Print column
print("Second Column:")
print(arr2[:,1])
print()


# ============================================
# Task 4: 3D Practice
# ============================================

print("========== TASK 4: 3D PRACTICE ==========\n")

arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

# Access layer
print("First Layer:")
print(arr3[0])
print()

# Access row inside layer
print("Row Inside Layer:")
print(arr3[0][1])
print()

# Access single element
print("Single Element:")
print(arr3[1][0][2])
print()


# ============================================
# Task 5: Slicing
# ============================================

print("========== TASK 5: SLICING ==========\n")

arr4 = np.array([10, 20, 30, 40, 50])

# Extract sub-array
print("Sub-array:")
print(arr4[1:4])
print()

# Step slicing
print("Step Slicing:")
print(arr4[::2])
print()

# Slice rows and columns
arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Slice Rows and Columns:")
print(arr5[:,1:3])
print()


# ============================================
# Task 6: Boolean Indexing
# ============================================

print("========== TASK 6: BOOLEAN INDEXING ==========\n")

arr6 = np.array([10, 20, 30, 40, 50])

# Filter values > 25
print("Values Greater Than 25:")
print(arr6[arr6 > 25])
print()

# Filter values between range
print("Values Between 10 and 40:")
print(arr6[(arr6 > 10) & (arr6 < 40)])
print()

# Replace values conditionally
print("Replace Values Greater Than 30 with 100:")

arr6[arr6 > 30] = 100

print(arr6)
print()


# ============================================
# End of Program
# ============================================

print("========== ALL TASKS COMPLETED ==========")