#find maximum and minimum
numbers = [10, 20, 5, 40, 15]

print("Max:", max(numbers))
print("Min:", min(numbers))
#find second largest
numbers = [10, 20, 5, 40, 15]

numbers = list(set(numbers))  
numbers.sort()

print("Second Largest:", numbers[-2])
#remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))
print(unique)
#count even and odd
numbers = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd) 
#reverse string
text = "hello"

print(text[::-1])
#check palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
#count characters
text = "hello"

print("Length:", len(text))
#count vowels and consonants
text = "hello"

vowels = "aeiou"
v_count = 0
c_count = 0

for char in text:
    if char in vowels:
        v_count += 1
    elif char.isalpha():
        c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
#create student list
students = {
    "A": 85,
    "B": 90,
    "C": 78
}

print(students)
#find topper list--------------------------------------------------------------------------
students = {
    "A": 85,
    "B": 90,
    "C": 78
}

topper = max(students, key=students.get)
print("Topper:", topper)
#calculate average--------------------------------------------------------------------
students = {
    "A": 85,
    "B": 90,
    "C": 78
}

avg = sum(students.values()) / len(students)
print("Average:", avg)
#filter passed student------------------------------------------------------------------
students = {
    "A": 85,
    "B": 40,
    "C": 78
}

passed = {k: v for k, v in students.items() if v >= 50}

print(passed)
#find second smallest
numbers = [10, 5, 8, 2, 3]

numbers = list(set(numbers))
numbers.sort()

print("Second Smallest:", numbers[1])
#merge two list without duplicates
list1 = [1, 2, 3]
list2 = [3, 4, 5]

merged = list(set(list1 + list2))

print(merged)
#find ferquency of element----------------------------------------------------------------------------------------
numbers = [1, 2, 2, 3, 3, 3]

freq = {}

for num in numbers:
    freq[num] = freq.get(num, 0) + 1

print(freq)
