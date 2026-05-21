# ============================================
# AI/ML Internship – Day 24
# Module 4: NumPy (Random Module & Dataset Simulation)
# ============================================

import numpy as np

# ============================================
# Task 1: Theory Answers
# ============================================

# 1. What is NumPy random module?
# NumPy random module is used to generate random numbers
# and random datasets.

# 2. Why random data is important?
# Random data helps to:
# - Simulate real-world data
# - Test ML models
# - Create sample datasets

# 3. What is seed?
# Seed ensures the same random output every time.
# It is useful for reproducibility.

# 4. Difference between randint() and rand()
# randint() -> Generates random integers
# rand()    -> Generates random decimal values

# 5. What is dataset simulation?
# Dataset simulation means creating artificial data
# similar to real-world data.


# ============================================
# Task 2: Random Integer Practice
# ============================================

print("----- Random Integer -----")
random_num = np.random.randint(1, 10)
print(random_num)

print("\n----- Array of Random Integers -----")
random_array = np.random.randint(1, 100, size=5)
print(random_array)

print("\n----- Random Matrix -----")
random_matrix = np.random.randint(1, 50, size=(3, 3))
print(random_matrix)


# ============================================
# Task 3: Random Decimal Practice
# ============================================

print("\n----- Random Decimal Values -----")
decimal_values = np.random.rand(3)
print(decimal_values)

print("\n----- 2D Decimal Matrix -----")
decimal_matrix = np.random.rand(2, 3)
print(decimal_matrix)


# ============================================
# Task 4: Random Choice
# ============================================

colors = ["red", "blue", "green"]

print("\n----- Random Color -----")
print(np.random.choice(colors))

print("\n----- Multiple Random Colors -----")
print(np.random.choice(colors, size=5))

names = ["Arun", "Meena", "Rahul", "Anu", "Kiran"]

print("\n----- Random Names -----")
print(np.random.choice(names, size=3))


# ============================================
# Task 5: Shuffle
# ============================================

print("\n----- Shuffle Array -----")
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

print("\n----- Shuffle Student IDs -----")
student_ids = np.array([101, 102, 103, 104, 105])
np.random.shuffle(student_ids)
print(student_ids)


# ============================================
# Task 6: Dataset Simulation
# ============================================

print("\n----- Marks Dataset -----")
marks = np.random.randint(40, 100, size=(5, 3))
print(marks)

# Rows -> Students
# Columns -> Subjects

print("\n----- Attendance Dataset -----")
attendance = np.random.randint(0, 2, size=(5, 5))
print(attendance)

# 1 = Present
# 0 = Absent

print("\n----- Random Image Matrix -----")
image = np.random.randint(0, 256, size=(3, 3))
print(image)

# Represents grayscale image pixels


# ============================================
# Random Seed Example
# ============================================

print("\n----- Random Seed Example -----")

np.random.seed(42)

seed_numbers = np.random.randint(1, 10, size=5)
print(seed_numbers)