# 1. Create list of 10 numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# 2. Sum of elements
print("Sum:", sum(numbers))

# 3. Maximum number
print("Max:", max(numbers))

# 4. Even numbers from list
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# 5. Reverse list
print("Reversed list:", numbers[::-1])
# 1. Create list of 10 numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# 2. Sum of elements
print("Sum:", sum(numbers))

# 3. Maximum number
print("Max:", max(numbers))

# 4. Even numbers from list
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# 5. Reverse list
print("Reversed list:", numbers[::-1])
# 1. Create dictionary
student = {
    "name": "Geethu",
    "age": 23,
    "marks": 85
}

# 2. Update marks
student["marks"] = 90

# 3. Add new key (grade)
student["grade"] = "A"

# 4. Print keys and values
for key, value in student.items():
    print(key, ":", value)
    text = "python"

# 1. Count characters
print("Length:", len(text))

# 2. Reverse string
print("Reversed:", text[::-1])

# 3. Palindrome check
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Count vowels
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)
# 1. Remove duplicates
list1 = [1,2,2,3,4,4,5]
unique = list(set(list1))
print("Unique list:", unique)

# 2. Common elements
set1 = {1,2,3,4}
set2 = {3,4,5,6}

common = set1 & set2
print("Common elements:", common)
# 1. Squares from 1–10
squares = [i*i for i in range(1, 11)]
print("Squares:", squares)

# 2. Even numbers from 1–20
evens = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers:", evens)s