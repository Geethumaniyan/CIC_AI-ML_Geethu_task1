text = "python programming"

# 1. Reverse string
print("Reversed:", text[::-1])

# 2. Count number of words
print("Word count:", len(text.split()))

# 3. Check palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Replace words
new_text = text.replace("python", "java")
print("Replaced:", new_text)

# 5. Count vowels
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print("Vowel count:", count)
# 1. List of students (name, marks)
students = [
    {"name": "A", "marks": 80},
    {"name": "B", "marks": 65},
    {"name": "C", "marks": 90},
    {"name": "D", "marks": 75},
    {"name": "E", "marks": 85}
]

# 2. Print all students
for s in students:
    print(s)

# 3. Average marks
avg = sum(s["marks"] for s in students) / len(students)
print("Average:", avg)

# 4. Highest marks
highest = max(s["marks"] for s in students)
print("Highest:", highest)

# 5. Students with marks > 75
print("Students with marks > 75:")
for s in students:
    if s["marks"] > 75:
        print(s["name"])
        import math
import random

# math module
print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))


#second higule.add(5, 3))hest
nums = [10, 20, 30, 40, 50]

nums = list(set(nums))  # remove duplicates
nums.sort()

print("Second highest:", nums[-2])
#count frequency
text = "python"

freq = {}

for char in text:
    freq[char] = freq.get(char, 0) + 1

print("Frequency:", freq)
#remove duplicates
nums = [1,2,2,3,4,4,5]

unique = []

for n in nums:
    if n not in unique:
        unique.append(n)

print("Without duplicates:", unique)
