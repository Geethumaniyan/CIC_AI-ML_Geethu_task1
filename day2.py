

# 1. Print details
name ="geethu"
age = 23
course = "Python"

print("Name:", name)
print("Age:", age)
print("Course:", course)

# 2. Add, subtract, multiply
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 3. Even or Odd
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Largest of two numbers
x = 20
y = 15

if x > y:
    print("Largest:", x)
else:
    print("Largest:", y)

# 5. Take input and display
name= input("Enter name: ")
print("You entered:", name)



# 1. Positive, Negative or Zero
num = int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Largest of 3 numbers
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if a > b and a > c:
    print("Largest:", a)
elif b > c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 3. Grade system
marks = int(input("Enter marks: "))

if marks > 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# 1. Print 1 to 20
for i in range(1, 21):
    print(i)

# 2. Even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. Sum of first N numbers
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)

# 4. Reverse 10 to 1
for i in range(10, 0, -1):
    print(i)


# 1. Add function
def add(a, b):
    return a + b

print("Add function:", add(5, 3))

# 2. Prime number function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Is Prime:", is_prime(7))

# 3. Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial:", factorial(5))