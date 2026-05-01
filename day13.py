# ===============================
# AI/ML Internship - Day 13 Tasks
# ===============================

# -------------------------------
# Task 1: Theory (Printed Output)
# -------------------------------

print("----- TASK 1: THEORY -----\n")

print("1. Debugging:")
print("Debugging is the process of finding and fixing errors in code.\n")

print("2. Types of Errors:")
print("Syntax Error: Wrong Python syntax")
print("Runtime Error: Error during execution")
print("Logical Error: Wrong output\n")

print("3. Optimization:")
print("Improving code to make it faster, cleaner, and efficient.\n")

print("4. Clean Code:")
print("Code that is easy to read, simple, and maintainable.\n")

print("5. Refactoring:")
print("Improving code without changing its output.\n")


# -------------------------------
# Task 2: Debugging Practice
# -------------------------------

print("----- TASK 2: DEBUGGING -----\n")

# Fix 1
print("Fix 1:")
print("Hello")

# Fix 2
print("\nFix 2:")
try:
    x = int("abc")
except ValueError:
    print("Invalid number")

# Fix 3
print("\nFix 3:")
nums = [1, 2, 3]

if len(nums) > 5:
    print(nums[5])
else:
    print("Index does not exist")


# -------------------------------
# Task 3: Optimization Practice
# -------------------------------

print("\n----- TASK 3: OPTIMIZATION -----\n")

nums = [5, 3, 8, 1]

# 1. Replace loop with sum()
total = sum(nums)
print("Sum:", total)

# 2. Optimized sorting
sorted_nums = sorted(nums)
print("Sorted:", sorted_nums)

# 3. Reduce repeated code
avg = total / len(nums)
print("Average:", avg)


# -------------------------------
# Task 4: Refactoring
# -------------------------------

print("\n----- TASK 4: REFACTORING -----\n")

# Reusable function
def get_sum(numbers):
    return sum(numbers)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print("Sum of nums1:", get_sum(nums1))
print("Sum of nums2:", get_sum(nums2))


# -------------------------------
# Extra: Real-world Example
# -------------------------------

print("\n----- EXTRA: AVERAGE FUNCTION -----\n")

def calculate_average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0

print("Average marks:", calculate_average([80, 90, 100]))
print("Average (empty list):", calculate_average([]))


# -------------------------------
# End of File