

# -----------------------------------
# Part 1: Inheritance
# -----------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

print("---- Inheritance ----")
s1 = Student("John", 85)
s1.display()
print("Marks:", s1.marks)


# -----------------------------------
# Part 2: Method Overriding
# -----------------------------------

class PersonOverride:
    def display(self):
        print("This is Person")

class StudentOverride(PersonOverride):
    def display(self):
        print("This is Student")

print("\n---- Method Overriding ----")
s = StudentOverride()
s.display()


# -----------------------------------
# Part 3: Encapsulation
# -----------------------------------

class StudentEncapsulation:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private variable

    def get_marks(self):
        return self.__marks

print("\n---- Encapsulation ----")
s2 = StudentEncapsulation("Sara", 90)
print("Marks:", s2.get_marks())


# -----------------------------------
# Part 4: Real-World Example
# -----------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

print("\n---- Real-World Example ----")
m = Manager("Alex", 50000, "IT")
print("Salary:", m.get_salary(), "| Department:", m.department)


# -----------------------------------
# Part 5: Types of Inheritance
# -----------------------------------

# Single Inheritance
class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

print("\n---- Single Inheritance ----")
dog = Dog()
dog.eat()
dog.sound()

# Multiple Inheritance
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

print("\n---- Multiple Inheritance ----")
c = C()
c.method_a()
c.method_b()


# -----------------------------------
# Task 2: Animal & Dog
# -----------------------------------

print("\n---- Task 2: Animal & Dog ----")
d = Dog()
d.eat()
d.sound()


# -----------------------------------
# Task 3: Method Overriding (Vehicle)
# -----------------------------------

class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

print("\n---- Task 3: Vehicle & Car ----")
car = Car()
car.start()


# -----------------------------------
# Task 4: Encapsulation (Bank Account)
# -----------------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        return self.__balance

print("\n---- Task 4: Bank Account ----")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.check_balance())


# -----------------------------------
# Task 5: Combined Practice
# -----------------------------------

class PersonBase:
    def __init__(self, name):
        self.name = name

class EmployeeDerived(PersonBase):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

print("\n---- Task 5: Person & Employee ----")
emp = EmployeeDerived("Geethu", 25000)
emp.display_details()


# -----------------------------------
# Theory Answers
# -----------------------------------

print("\n---- Theory Answers ----")
print("1. Inheritance: Reusing properties and methods from another class.")
print("2. Method Overriding: Child class modifies parent class method.")
print("3. Encapsulation: Hiding data and controlling access.")
print("4. Private Variable: Variable declared using __ (double underscore).")
print("5. OOP Use: Code reuse, modularity, easy maintenance.")