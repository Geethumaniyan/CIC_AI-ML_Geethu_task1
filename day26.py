# ============================================
# AI/ML Internship – Day 26
# Module 5: Pandas Introduction
# ============================================

# ==================================================
# Part 1: Import Pandas
# ==================================================

import pandas as pd


# ==================================================
# Task 1: Theory Answers
# ==================================================

# 1. What is Pandas?
# Pandas is a Python library used for working with structured data.
# It is mainly used for data analysis and data manipulation.

# 2. Why Pandas is important?
# Pandas helps:
# - Analyze data
# - Clean messy datasets
# - Handle missing values
# - Process datasets quickly

# 3. What is Series?
# Series is a one-dimensional data structure in Pandas.
# It is similar to a NumPy 1D array.

# 4. What is DataFrame?
# DataFrame is a table-like data structure in Pandas.
# It contains rows and columns like an Excel sheet.

# 5. Difference between NumPy and Pandas
# NumPy:
# - Used for numerical operations
# - Works with arrays
# - Faster mathematical calculations

# Pandas:
# - Used for data analysis
# - Works with DataFrames and tables
# - Easier data handling and cleaning


# ==================================================
# Task 2: Series Practice
# ==================================================

print("===== Task 2: Series Practice =====")

# 1. Create Series
series1 = pd.Series([10, 20, 30, 40])

print("Simple Series:")
print(series1)

# 2. Create Series with custom index
series2 = pd.Series(
    [85, 90, 78],
    index=["Math", "Science", "English"]
)

print("\nSeries with Custom Index:")
print(series2)

# 3. Access Series values
print("\nAccess Specific Value:")
print(series2["Math"])


# ==================================================
# Task 3: DataFrame Practice
# ==================================================

print("\n===== Task 3: DataFrame Practice =====")

# 1. Create DataFrame using dictionary
data = {
    "Name": ["Rahul", "Anu", "Arjun"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# 2. Print DataFrame
print("Original DataFrame:")
print(df)

# 3. Add one more column
df["Grade"] = ["A", "A+", "B"]

print("\nDataFrame After Adding Grade Column:")
print(df)


# ==================================================
# Task 4: Data Access
# ==================================================

print("\n===== Task 4: Data Access =====")

# 1. Access single column
print("Single Column - Name:")
print(df["Name"])

# 2. Access multiple columns
print("\nMultiple Columns - Name and Marks:")
print(df[["Name", "Marks"]])

# 3. Print specific rows
print("\nFirst Two Rows:")
print(df.iloc[0:2])


# ==================================================
# Task 5: Data Information
# ==================================================

print("\n===== Task 5: Data Information =====")

# 1. head()
print("Head Function:")
print(df.head())

# 2. tail()
print("\nTail Function:")
print(df.tail())

# 3. info()
print("\nInfo Function:")
print(df.info())