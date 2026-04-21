

# 1. Create file with student data
with open("students.txt", "w") as f:
    f.write("Anu,85\nRahul,78\nMeena,92\nArjun,67\nDiya,74\n")

# 2. Read and store in list of dictionaries
students = []
with open("students.txt", "r") as f:
    for line in f:
        name, marks = line.strip().split(",")
        students.append({"name": name, "marks": int(marks)})

# 3. Print all students
print("All Students:")
for s in students:
    print(s)

# 4. Find average marks
total = sum(s["marks"] for s in students)
avg = total / len(students)
print("\nAverage Marks:", avg)

# 5. Find topper
topper = max(students, key=lambda x: x["marks"])
print("Topper:", topper)


# Task 3: Data Processing Programs

# 1. Filter students with marks > 75
high_scorers = [s for s in students if s["marks"] > 75]
print("\nStudents with marks > 75:", high_scorers)

# 2. Count number of students
print("Total Students:", len(students))

# 3. Find lowest marks
lowest = min(students, key=lambda x: x["marks"])
print("Lowest Marks:", lowest)

# 4. Sort students by marks
sorted_students = sorted(students, key=lambda x: x["marks"])
print("Sorted Students:", sorted_students)


# Task 4: Function Practice

def calculate_average(students):
    total = sum(s["marks"] for s in students)
    return total / len(students)

def find_topper(students):
    return max(students, key=lambda x: x["marks"])

def filter_students(students, threshold=75):
    return [s for s in students if s["marks"] > threshold]

print("\nUsing Functions:")
print("Average:", calculate_average(students))
print("Topper:", find_topper(students))
print("Filtered:", filter_students(students))


# Task 5: Logic Challenge

# 1. Second highest marks
sorted_students_desc = sorted(students, key=lambda x: x["marks"], reverse=True)
second_highest = sorted_students_desc[1]
print("\nSecond Highest:", second_highest)

# 2. Count pass/fail (pass mark = 50)
pass_count = sum(1 for s in students if s["marks"] >= 50)
fail_count = sum(1 for s in students if s["marks"] < 50)

print("Pass:", pass_count)
print("Fail:", fail_count)

# 3. Convert to dictionary format
student_dict = {s["name"]: s["marks"] for s in students}
print("Dictionary Format:", student_dict)