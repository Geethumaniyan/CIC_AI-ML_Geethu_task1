#function to find factorial
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result
print(factorial(5))
#function to check prime number
def is_prime(n):
    if n <= 1:
        return "Not Prime"
    
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    
    return "Prime"

print(is_prime(7))
print(is_prime(10))
#reverse string
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))
#function to calculate average
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(calculate_average([10, 20, 30, 40]))
#factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
#sum of numbers using recursion
def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

print(sum_numbers(5))
#fibonacci series using recursion
# fibonacci series using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(6):
    print(fibonacci(i), end=" ")

# square all numbers
nums = [1, 2, 3, 4]
result = list(map(lambda x: x**2, nums))
print(result)
#double all values
nums = [1, 2, 3]
result = list(map(lambda x: x*2, nums))
print(result)
#convert list to uppercase
words = ["apple", "banana", "cherry"]
result = list(map(lambda x: x.upper(), words))
print(result)
#find even numbers
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)
#filter students with mark>50
marks = [40, 60, 75, 30, 90]
result = list(filter(lambda x: x > 50, marks))
print(result)
#filter words with length>5
words = ["apple", "banana", "kiwi", "grapes"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)
#flatten nested list
def flatten_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print(flatten_list([1, [2, [3, 4], 5]]))
#count occurences using dictionary
def count_occurrences(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


print(count_occurrences([1, 2, 2, 3, 3, 3]))
