# =========================================
# AI/ML Internship – Day 29
# Pandas: Sorting, Grouping & Data Analysis
# =========================================

import pandas as pd

# -----------------------------------------
# Create Dataset
# -----------------------------------------

data = {
    "Name": ["Rahul", "Anu", "Arjun", "Meera"],
    "Department": ["AI", "Web", "AI", "Web"],
    "City": ["Delhi", "Kochi", "Delhi", "Mumbai"],
    "Category": ["A", "B", "A", "B"],
    "Salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# =========================================
# Task 1: Theory Answers
# =========================================

print("\n1. What is sorting?")
print("Sorting means arranging data in ascending or descending order.")

print("\n2. Why sorting is important?")
print("Sorting helps find highest and lowest values and organize data.")

print("\n3. What is grouping?")
print("Grouping means combining rows with similar values.")

print("\n4. What is aggregation?")
print("Aggregation means summarizing grouped data using functions like sum and average.")

print("\n5. What is data analysis?")
print("Data analysis means finding patterns and useful insights from data.")

# =========================================
# Task 2: Sorting Practice
# =========================================

print("\nSort Salary Ascending")
print(df.sort_values("Salary"))

print("\nSort Salary Descending")
print(df.sort_values("Salary", ascending=False))

print("\nSort by Multiple Columns")
print(df.sort_values(["Department", "Salary"]))

# =========================================
# Task 3: Grouping Practice
# =========================================

print("\nGroup by Department")
print(df.groupby("Department"))

print("\nGroup by City")
print(df.groupby("City"))

print("\nGroup by Category")
print(df.groupby("Category"))

# =========================================
# Task 4: Aggregation Practice
# =========================================

print("\nAverage Salary")
print(df.groupby("Department")["Salary"].mean())

print("\nTotal Salary")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count")
print(df.groupby("Department")["Name"].count())

# =========================================
# Task 5: Multiple Aggregation
# =========================================

print("\nMean, Max, Min Salary")
print(
    df.groupby("Department")["Salary"].agg(["mean", "max", "min"])
)

# =========================================
# Task 6: Value Counts
# =========================================

print("\nCount Departments")
print(df["Department"].value_counts())

print("\nCount Repeated Values")
print(df["Category"].value_counts())

print("\nAnalyze Category Frequency")
print(df["Category"].value_counts(normalize=True))

# =========================================
# End of Program
# =========================================