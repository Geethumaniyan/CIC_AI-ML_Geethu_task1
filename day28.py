# ============================================
# AI/ML Internship – Day 28
# Module 5: Pandas (Handling Missing Data & Data Cleaning)
# ============================================

import pandas as pd
import numpy as np


# ==================================================
# Task 1: Theory Answers
# ==================================================

# 1. What is missing data?
# Missing data means some values are empty or unavailable
# in the dataset.

# 2. Why data cleaning is important?
# Data cleaning is important because dirty data can cause:
# - Wrong predictions
# - Poor machine learning performance
# - Incorrect analysis

# 3. What is isnull()?
# isnull() is used to detect missing values in a dataset.

# 4. What is dropna()?
# dropna() removes rows or columns containing missing values.

# 5. What is fillna()?
# fillna() replaces missing values with custom values.


# ==================================================
# Task 2: Missing Data Practice
# ==================================================

print("===== Task 2: Missing Data Practice =====")

# 1. Create dataset with missing values
data = {
    "Name": ["Rahul", "Anu", "Arjun", None],
    "Marks": [85, np.nan, 78, 90],
    "City": ["Kochi", "Trivandrum", None, "Kollam"]
}

df = pd.DataFrame(data)

print("Dataset with Missing Values:")
print(df)

# 2. Detect missing values
print("\nMissing Values Detection:")
print(df.isnull())

# 3. Count missing values
print("\nCount Missing Values:")
print(df.isnull().sum())


# ==================================================
# Task 3: Remove Missing Data
# ==================================================

print("\n===== Task 3: Remove Missing Data =====")

# 1. Drop rows with missing values
print("Drop Rows with Missing Values:")
print(df.dropna())

# 2. Drop columns with missing values
print("\nDrop Columns with Missing Values:")
print(df.dropna(axis=1))


# ==================================================
# Task 4: Fill Missing Data
# ==================================================

print("\n===== Task 4: Fill Missing Data =====")

# 1. Fill with text
print("Fill Missing Values with Text:")
print(df.fillna("Unknown"))

# 2. Fill with mean value
mean_marks = df["Marks"].mean()

df["Marks"] = df["Marks"].fillna(mean_marks)

print("\nFill Missing Marks with Mean:")
print(df)

# 3. Fill numeric columns
df["Marks"] = df["Marks"].fillna(0)

print("\nNumeric Column After Filling:")
print(df)


# ==================================================
# Task 5: Duplicate Handling
# ==================================================

print("\n===== Task 5: Duplicate Handling =====")

# 1. Create duplicate rows
duplicate_df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

print("Dataset with Duplicate Row:")
print(duplicate_df)

# 2. Detect duplicates
print("\nDetect Duplicates:")
print(duplicate_df.duplicated())

# 3. Remove duplicates
print("\nRemove Duplicates:")
print(duplicate_df.drop_duplicates())


# ==================================================
# Task 6: Column Operations
# ==================================================

print("\n===== Task 6: Column Operations =====")

# 1. Rename columns
df.rename(columns={"Marks": "Score"}, inplace=True)

print("After Renaming Column:")
print(df)

# 2. Change data type
df["Score"] = df["Score"].astype(int)

# 3. Print data types
print("\nData Types:")
print(df.dtypes)