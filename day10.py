

# -----------------------------------
# Part 1 & 2: Class and Object
# -----------------------------------

class StudentBasic:
    name = ""
    marks = 0

print("---- Class & Object ----")
s1 = StudentBasic()
s1.name = "John"
s1.marks = 85
print(s1.name, s1.marks)


# -----------------------------------
# Part 3: Constructor (__init__)
# -----------------------------------

class StudentConstructor:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

print("\n---- Constructor ----")
s2 = StudentConstructor("Sara", 90)
print(s2.name, s2.marks)


# -----------------------------------
# Part 4: Methods in Class
# -----------------------------------

class StudentMethod:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

print("\n---- Method Example ----")
s3 = StudentMethod("Alex", 75)
s3.display()


# -----------------------------------
# Part 5: Real-World Example
# -----------------------------------

class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

print("\n---- Pass/Fail Check ----")
s4 = StudentResult("John", 40)
print(s4.name, s4.is_pass())


# -----------------------------------
# Part 6: Multiple Objects
# -----------------------------------

print("\n---- Multiple Objects ----")
students = [
    StudentResult("A", 70),
    StudentResult("B", 90),
    StudentResult("C", 40)
]

for s in students:
    print(s.name, s.marks, "-", s.is_pass())


# -----------------------------------
# Task 2: Class Practice (Car)
# -----------------------------------

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

print("\n---- Task 2: Car ----")
car1 = Car("BMW", 5000000)
print("Car:", car1.name, "| Price:", car1.price)


# -----------------------------------
# Task 3: Constructor Practice
# -----------------------------------

print("\n---- Task 3: Student Constructor ----")
student1 = StudentConstructor("Geethu", 88)
print(student1.name, student1.marks)


# -----------------------------------
# Task 4: Method Practice
# -----------------------------------

class StudentGrade:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass(self):
        return "Pass" if self.marks >= 50 else "Fail"

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"

print("\n---- Task 4: Pass/Fail & Grade ----")
sg = StudentGrade("Rahul", 82)
print(sg.name, sg.check_pass(), sg.calculate_grade())


# -----------------------------------
# Task 5: Object List
# -----------------------------------

print("\n---- Task 5: Student List ----")
student_list = [
    StudentGrade("A", 70),
    StudentGrade("B", 95),
    StudentGrade("C", 60)
]

# Print all students
for s in student_list:
    print(s.name, s.marks, s.calculate_grade())

# Find topper
topper = max(student_list, key=lambda x: x.marks)
print("Topper:", topper.name, topper.marks)


# -----------------------------------
# Task 7: Logic Challenge (BankAccount)
# -----------------------------------

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.balance

print("\n---- Task 7: Bank Account ----")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.check_balance())


# -----------------------------------
# Task 7: Product Class
# -----------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_discount(self, percent):
        discount = self.price * (percent / 100)
        return self.price - discount

print("\n---- Task 7: Product ----")
p1 = Product("Laptop", 50000)
print("Final Price after discount:", p1.calculate_discount(10))


# -----------------------------------
# Theory Answers
# -----------------------------------

print("\n---- Theory Answers ----")

print("1. OOP: Programming using classes and objects.")
print("2. Class vs Object: Class is blueprint, object is instance.")
print("3. Constructor: Special method (__init__) to initialize values.")
print("4. Method: Function inside a class.")
print("5. Why OOP: Reusability, structure, easy maintenance.")