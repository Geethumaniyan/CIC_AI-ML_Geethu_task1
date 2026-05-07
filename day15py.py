# Create list of marks
marks = [80, 90, 70, 60, 50]

# Find average
avg = sum(marks) / len(marks)
print("Average:", avg)

# Find max and min
print("Max:", max(marks))
print("Min:", min(marks))

# Count total students
print("Total Students:", len(marks))
#data cleaning-----------

marks = [80, 90, None, -10, 70, -5]

# Remove None values
cleaned = [m for m in marks if m is not None]

# Remove negative values
cleaned = [m for m in cleaned if m >= 0]

print("Cleaned Data:", cleaned)
marks = [80, 40, 90, 30, 75, 60]
#data filtering-------------

# Passed students (>=50)
passed = [m for m in marks if m >= 50]
print("Passed:", passed)

# Marks > 75
above_75 = [m for m in marks if m > 75]
print("Above 75:", above_75)

# Even numbers
even = [m for m in marks if m % 2 == 0]
print("Even Marks:", even)
# data transformation----------
marks = [80, 90, 70]
# Convert to percentage (0–1 scale)
percentage = [m / 100 for m in marks]
print("Percentage:", percentage)

# Multiply values (example ×2)
multiplied = [m * 2 for m in marks]
print("Multiplied:", multiplied)

# Normalize data (divide by max value)
max_val = max(marks)
normalized = [m / max_val for m in marks]
print("Normalized:", normalized)