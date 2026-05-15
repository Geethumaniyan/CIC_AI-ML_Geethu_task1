# AI/ML Internship – Day 22
# Module 4: NumPy (Aggregations & Statistics)

import numpy as np

print("===== Task 1: Theory Answers =====")

# 1. Aggregation Functions
print("\n1. What are Aggregation Functions?")
print("Aggregation functions combine multiple values into a single value.")
print("Examples: sum, mean, max, min")

# 2. Mean
print("\n2. What is Mean?")
print("Mean is the average value of data.")

# Formula:
# Mean = Sum of values / Number of values

# 3. Median
print("\n3. What is Median?")
print("Median is the middle value after sorting the data.")

# 4. Standard Deviation
print("\n4. What is Standard Deviation?")
print("Standard deviation measures how much data varies from the mean.")

# 5. Axis
print("\n5. What is Axis?")
print("axis=0 means column-wise operation")
print("axis=1 means row-wise operation")


print("\n===== Task 2: Basic Aggregation =====")

arr = np.array([10, 20, 30, 40])

# Sum
print("\n1. Sum")
print(np.sum(arr))

# Mean
print("\n2. Mean")
print(np.mean(arr))

# Maximum and Minimum
print("\n3. Maximum and Minimum")
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))


print("\n===== Task 3: Statistical Functions =====")

# Median
print("\n1. Median")
print(np.median(arr))

# Standard Deviation
print("\n2. Standard Deviation")
print(np.std(arr))

# Variance
print("\n3. Variance")
print(np.var(arr))


print("\n===== Task 4: Axis Practice =====")

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOriginal Array:")
print(arr2)

# Row-wise Sum
print("\n1. Row-wise Sum (axis=1)")
print(np.sum(arr2, axis=1))

# Column-wise Sum
print("\n2. Column-wise Sum (axis=0)")
print(np.sum(arr2, axis=0))

# Mean using axis
print("\n3. Mean using axis")

print("Column-wise Mean:")
print(np.mean(arr2, axis=0))

print("Row-wise Mean:")
print(np.mean(arr2, axis=1))


print("\n===== Task 5: Index Functions =====")

# Index of Maximum Value
print("\n1. Index of Maximum Value")
print(np.argmax(arr))

# Index of Minimum Value
print("\n2. Index of Minimum Value")
print(np.argmin(arr))


print("\n===== Task 6: Cumulative Operations =====")

arr3 = np.array([1, 2, 3, 4])

# Cumulative Sum
print("\n1. Cumulative Sum")
print(np.cumsum(arr3))

# Analysis
print("\n2. Analysis")
print("Cumulative sum adds values continuously.")
print("1")
print("1 + 2 = 3")
print("1 + 2 + 3 = 6")
print("1 + 2 + 3 + 4 = 10")

print("\n===== Program Completed =====")