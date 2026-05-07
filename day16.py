#cleaning practice
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": None},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": -10}
]

# Keep only valid data
cleaned = []

for s in students:
    if s["marks"] is not None and s["marks"] >= 0:
        cleaned.append(s)

print(cleaned)
#transformation
students = [
    {"name": "A", "marks": 80},
    {"name": "C", "marks": 40}
]

for s in students:

    # Pass/Fail
    s["status"] = "Pass" if s["marks"] >= 50 else "Fail"

    # Percentage
    s["percentage"] = s["marks"]

    # New calculated field
    s["double_marks"] = s["marks"] * 2

print(students)
#sorting
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 95},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": 70}
]

# Sort by marks
students.sort(key=lambda x: x["marks"], reverse=True)

print("Sorted Students:")
print(students)

# Top 3 students
print("\nTop 3 Students:")
print(students[:3])
#grouping
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 45},
    {"name": "C", "marks": 60},
    {"name": "D", "marks": 30}
]

result = {"pass": [], "fail": []}

for s in students:
    if s["marks"] >= 50:
        result["pass"].append(s)
    else:
        result["fail"].append(s)

print(result)

# Count groups
print("\nPass Count:", len(result["pass"]))
print("Fail Count:", len(result["fail"]))
#data analysis
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 95},
    {"name": "C", "marks": 40},
    {"name": "D", "marks": 70}
]

marks = [s["marks"] for s in students]

# Average
average = sum(marks) / len(marks)

# Highest
highest = max(marks)

# Lowest
lowest = min(marks)

print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
