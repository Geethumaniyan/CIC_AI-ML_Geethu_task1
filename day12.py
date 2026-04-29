# ==============================
# AI/ML Internship - Day 12
# Module 3: Python for AI
# ==============================

# ------------------------------
# Task 1: Theory (Printed Output)
# ------------------------------
print("TASK 1: THEORY")
print("1. List Comprehension: Short way to create lists")
print("2. List vs Set: List allows duplicates, Set does not")
print("3. Generator: Uses yield to produce values one by one")
print("4. Zip: Combines multiple lists")
print("5. Enumerate: Adds index to elements")
print("\n")


# ------------------------------
# Task 2: List Comprehension
# ------------------------------
print("TASK 2: LIST COMPREHENSION")

# 1. Square numbers
nums = [2, 5, 4, 6, 7]
squares = [x*x for x in nums]
print("Squares:", squares)

# 2. Find even numbers
nums = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in nums if x % 2 == 0]
print("Even numbers:", even)

# 3. Convert strings to uppercase
names = ["Aswin", "Janaki", "Revathy"]
upper = [n.upper() for n in names]
print("Uppercase:", upper)

# 4. Filter numbers > 50
nums = [10,20,30,40,50,55,60,65,70,90,80]
greater = [x for x in nums if x > 50]
print("Greater than 50:", greater)
print("\n")


# ------------------------------
# Task 3: Dictionary Comprehension
# ------------------------------
print("TASK 3: DICTIONARY COMPREHENSION")

# 1. Number-square dictionary
nums = [2,3,4,5,6]
square_dict = {x: x*x for x in nums}
print("Square dict:", square_dict)

# 2. Filter even numbers
even_dict = {x: x for x in range(1, 20) if x % 2 == 0}
print("Even dict:", even_dict)

# 3. Map names to length
names = ["Revathy", "Anu", "John"]
name_length = {name: len(name) for name in names}
print("Name lengths:", name_length)
print("\n")


# ------------------------------
# Task 4: Set Practice
# ------------------------------
print("TASK 4: SET PRACTICE")

# 1. Remove duplicates
nums = [1,2,2,3,3,4,4,5,5,6,7,8,9,9,10]
unique = set(nums)
print("Unique numbers:", unique)

# 2. Find common elements
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
common = set1 & set2
print("Common elements:", common)

# 3. Union and difference
print("Union:", set1 | set2)
print("Difference:", set1 - set2)
print("\n")


# ------------------------------
# Task 5: Generator Practice
# ------------------------------
print("TASK 5: GENERATORS")

# 1. Generator for numbers
def number_generator(n):
    for i in range(n):
        yield i

print("Number Generator:")
for num in number_generator(10):
    print(num, end=" ")
print("\n")

# 2. Even numbers generator
def even_generator(n):
    for i in range(0, n, 2):
        yield i

print("Even Generator:")
for num in even_generator(20):
    print(num, end=" ")
print("\n")

# 3. Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci:")
for num in fibonacci(7):
    print(num, end=" ")
print("\n\n")


# ------------------------------
# Task 6: Zip & Enumerate
# ------------------------------
print("TASK 6: ZIP & ENUMERATE")

names = ["Revathy","Aswin","Janaki","Madhav"]
marks = [95,85,99,82]

# 1. Combine lists
combined = list(zip(names, marks))
print("Combined:", combined)

# 2. Print index + value
print("Enumerate:")
for i, name in enumerate(names):
    print(i, name)

# 3. Convert zip to dictionary
data = dict(zip(names, marks))
print("Dictionary:", data)
