# ============================================
# AI/ML Internship – Day 25
# Module 4: NumPy (Real-World Problems & Practice)
# ============================================

import numpy as np

# ==================================================
# Task 1: Theory Answers
# ==================================================

# 1. Why NumPy is important?
# NumPy is important because it provides:
# - Fast computations
# - Efficient data handling
# - Matrix operations
# - Mathematical calculations used in AI/ML

# 2. What is vectorization?
# Vectorization means performing operations on entire arrays
# without using loops. It is faster and more efficient.

# 3. Why shape matters in ML?
# Machine Learning models expect data in specific shapes.
# Incorrect shapes can cause errors during training.

# 4. What is normalization?
# Normalization means scaling data into a smaller range,
# usually between 0 and 1.

# 5. What is feature extraction?
# Feature extraction means selecting useful information
# from raw data for machine learning.


# ==================================================
# Task 2: Marks Analysis
# ==================================================

print("===== Task 2: Marks Analysis =====")

marks = np.array([
    [85, 78, 90],
    [70, 88, 60],
    [95, 92, 89]
])

print("Marks Matrix:")
print(marks)

# Average marks
average_marks = np.mean(marks)
print("Average Marks:", average_marks)

# Highest marks
highest_marks = np.max(marks)
print("Highest Marks:", highest_marks)

# Lowest marks
lowest_marks = np.min(marks)
print("Lowest Marks:", lowest_marks)

# Find topper
total_marks = np.sum(marks, axis=1)
print("Total Marks of Students:", total_marks)

topper = np.argmax(total_marks)
print("Top Student Index:", topper)


# ==================================================
# Task 3: Image Operations
# ==================================================

print("\n===== Task 3: Image Operations =====")

image = np.array([
    [50, 100],
    [150, 200]
])

print("Original Image:")
print(image)

# Increase brightness
bright_image = image + 50
print("Brightness Increased:")
print(bright_image)

# Decrease brightness
dark_image = image - 30
print("Brightness Decreased:")
print(dark_image)

# Normalize image pixels
normalized_image = image / 255
print("Normalized Image:")
print(normalized_image)


# ==================================================
# Task 4: Dataset Filtering
# ==================================================

print("\n===== Task 4: Dataset Filtering =====")

arr = np.array([10, 55, 80, 25, 90, 45, 60])

print("Original Array:")
print(arr)

# Filter values > 50
filtered_values = arr[arr > 50]
print("Values Greater Than 50:")
print(filtered_values)

# Replace low values
arr[arr < 50] = 0
print("After Replacing Low Values:")
print(arr)

# Count filtered values
count_filtered = np.sum(filtered_values > 50)
print("Count of Values > 50:", count_filtered)


# ==================================================
# Task 5: Reshaping
# ==================================================

print("\n===== Task 5: Reshaping =====")

# Convert 1D → 2D
array_1d = np.arange(12)
print("1D Array:")
print(array_1d)

array_2d = array_1d.reshape(3, 4)
print("Converted to 2D:")
print(array_2d)

# Convert 2D → 1D
back_to_1d = array_2d.flatten()
print("Converted Back to 1D:")
print(back_to_1d)

# Create 3D dataset
array_3d = np.arange(24).reshape(2, 3, 4)
print("3D Dataset:")
print(array_3d)


# ==================================================
# Task 6: Dataset Simulation
# ==================================================

print("\n===== Task 6: Dataset Simulation =====")

# Attendance matrix
attendance = np.random.randint(0, 2, size=(5, 7))
print("Attendance Dataset:")
print(attendance)

# Marks dataset
marks_dataset = np.random.randint(35, 100, size=(5, 3))
print("Marks Dataset:")
print(marks_dataset)

# Weather dataset
weather = np.random.randint(20, 40, size=(7,))
print("Weather Dataset:")
print(weather)