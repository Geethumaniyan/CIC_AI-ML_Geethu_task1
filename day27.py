# ============================================
# AI/ML Internship – Day 27
# Module 5: Pandas (Reading CSV Files & Data Selection)
# ============================================

import pandas as pd


# ==================================================
# Task 1: Theory Answers
# ==================================================

# 1. What is CSV file?
# CSV stands for Comma Separated Values.
# It stores data in table format separated by commas.

# 2. Why CSV files are important?
# CSV files are important because:
# - They store structured data
# - They are simple and lightweight
# - They work with Excel and databases
# - They are widely used in AI/ML projects

# 3. What is read_csv()?
# read_csv() is a Pandas function used to read CSV files
# and load them into a DataFrame.

# 4. Difference between loc and iloc
# loc:
# - Uses labels
# - Name-based selection

# iloc:
# - Uses index positions
# - Number-based selection

# 5. What is data filtering?
# Data filtering means selecting only required data
# based on conditions.


# ==================================================
# Task 2: CSV Practice
# ==================================================

print("===== Task 2: CSV Practice =====")

# Create sample dataset
data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Marks": [85, 90, 78, 95],
    "City": ["Kochi", "Trivandrum", "Kollam", "Kochi"]
}

df = pd.DataFrame(data)

# Create CSV file
df.to_csv("students.csv", index=False)

print("CSV File Created Successfully!")

# Read CSV file
students = pd.read_csv("students.csv")

# Print dataset
print("\nDataset:")
print(students)


# ==================================================
# Task 3: Column Selection
# ==================================================

print("\n===== Task 3: Column Selection =====")

# 1. Select single column
print("Single Column - Name:")
print(students["Name"])

# 2. Select multiple columns
print("\nMultiple Columns - Name and Marks:")
print(students[["Name", "Marks"]])

# 3. Print specific column values
print("\nMarks Column Values:")
print(students["Marks"].values)


# ==================================================
# Task 4: Row Selection
# ==================================================

print("\n===== Task 4: Row Selection =====")

# 1. Select row using loc
print("Row Using loc:")
print(students.loc[0])

# 2. Select row using iloc
print("\nRow Using iloc:")
print(students.iloc[1])

# 3. Slice rows
print("\nRow Slicing:")
print(students[0:2])


# ==================================================
# Task 5: Filtering
# ==================================================

print("\n===== Task 5: Filtering =====")

# 1. Filter marks > 80
print("Students with Marks > 80:")
print(students[students["Marks"] > 80])

# 2. Filter city names
print("\nStudents from Kochi:")
print(students[students["City"] == "Kochi"])

# 3. Combine conditions
print("\nStudents with Marks > 80 and City = Kochi:")
print(
    students[
        (students["Marks"] > 80) &
        (students["City"] == "Kochi")
    ]
)


# ==================================================
# Additional Data Information
# ==================================================

print("\n===== Additional Data Information =====")

# Head function
print("Head Function:")
print(students.head())

# Tail function
print("\nTail Function:")
print(students.tail())

# Shape function
print("\nShape of Dataset:")
print(students.shape)