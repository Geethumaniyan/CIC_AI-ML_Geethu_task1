# 1. Create file and write details
with open("details.txt", "w") as f:
    f.write("Name: Geethu\n")
    f.write("Age: 23\n")
    f.write("Course: Python\n")

# 2. Read file and display
with open("details.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# 3. Append new data
with open("details.txt", "a") as f:
    f.write("City: Calicut\n")

# 4. Count number of lines
with open("details.txt", "r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))

# 5. Count number of words
with open("details.txt", "r") as f:
    words = f.read().split()
    print("Number of words:", len(words))
    # 1. Handle divide by zero
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Handle invalid input
try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input! Please enter a number")

# 3. try-except-else-finally
try:
    x = int(input("Enter number: "))
    y = int(input("Enter another: "))
    result = x / y
except Exception as e:
    print("Error:", e)
else:
    print("Result:", result)
finally:
    print("Execution completed")

# 4. Handle file not found
try:
    with open("file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
    sentence = input("Enter a sentence: ")
words = sentence.split()

longest = max(words, key=len)

print("Longest word:", longest)
#find longest word in file
with open("details.txt", "r") as f:
    words = f.read().split()

longest = max(words, key=len)


print("Longest word:", longest)
#count vowels in file
with open("details.txt", "r") as f:
    text = f.read().lower()

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count +=1

print("Total vowels:", count)
# remove duplicate lines
with open("details.txt", "r") as f:
    lines = f.readlines()

unique_lines = []

for line in lines:
    clean_line = line.strip()
    if clean_line not in unique_lines:
        unique_lines.append(clean_line)

with open("details.txt", "w") as f:
    for line in unique_lines:
        f.write(line + "\n")

print("Duplicate lines removed")

