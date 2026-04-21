

# Variables & Data Types
name = "Geethu"
age = 25
marks = 85.5
print("Name:", name, "| Age:", age, "| Marks:", marks)

# Input / Output
# user_input = input("Enter something: ")
# print("You entered:", user_input)

# Operators
a, b = 10, 5
print("Addition:", a + b)
print("Comparison:", a > b)

# If-Else
if a > b:
    print("A is greater")
else:
    print("B is greater")

# Loops
print("\nFor Loop:")
for i in range(3):
    print(i)

print("While Loop:")
i = 0
while i < 3:
    print(i)
    i += 1

# Data Structures
my_list = [1, 2, 3]
my_dict = {"name": "Geethu", "age": 25}
my_set = {1, 2, 2, 3}
print("List:", my_list)
print("Dictionary:", my_dict)
print("Set:", my_set)

# Function
def add(x, y):
    return x + y

print("Function Output:", add(2, 3))

# File Handling
with open("sample.txt", "w") as f:
    f.write("Hello AI/ML")

with open("sample.txt", "r") as f:
    print("File Content:", f.read())

# Exception Handling
try:
    x = int("abc")
except:
    print("Error occurred!")
finally:
    print("Finally block executed")

# Part 2: Pattern Programs


print("\nStar Pattern:")
for i in range(1, 5):
    print("*" * i)

print("\nNumber Pattern:")
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


# Part 3: Assessment Coding

# Q1: Palindrome
def is_palindrome(s):
    return s == s[::-1]

print("\nPalindrome Check:", is_palindrome("madam"))

# Q2: Largest in list
def find_largest(lst):
    return max(lst)

print("Largest:", find_largest([10, 20, 5, 30]))

# Q3: Count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

print("Vowels Count:", count_vowels("Artificial Intelligence"))

# Q4: Dictionary
student = {"name": "Geethu", "marks": 90}
print("Dictionary Values:", student.values())


# Section C: Mini Task


students = []
for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    students.append(mark)

avg = sum(students) / len(students)
topper = max(students)

print("Average:", avg)
print("Topper Marks:", topper)


# Extra Task

# 1. Reverse list
def reverse_list(lst):
    return lst[::-1]

print("Reversed:", reverse_list([1, 2, 3, 4]))

# 2. Count words
def count_words(s):
    return len(s.split())

print("Word Count:", count_words("AI and ML Internship"))

# 3. Remove duplicates
def remove_duplicates(lst):
    return list(set(lst))

print("No Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4]))

# 4. Second largest
def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

print("Second Largest:", second_largest([10, 20, 30, 40]))