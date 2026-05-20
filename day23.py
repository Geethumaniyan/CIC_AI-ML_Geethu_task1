# ==========================================
# AI/ML Internship – Day 23
# Module 4: NumPy Broadcasting
# ==========================================

import numpy as np

print("===== Task 1: Theory Answers =====")

# 1
print("\n1. What is broadcasting?")
print("Broadcasting is the automatic expansion of smaller arrays")
print("during operations with larger arrays.")

# 2
print("\n2. Why broadcasting is important?")
print("Broadcasting reduces loops, improves speed,")
print("and makes code simpler and memory efficient.")

# 3
print("\n3. What are broadcasting rules?")
print("Two dimensions are compatible when:")
print("1. They are equal")
print("OR")
print("2. One of them is 1")

# 4
print("\n4. What happens with incompatible shapes?")
print("NumPy gives an error when shapes are incompatible.")

# 5
print("\n5. Advantages of broadcasting")
print("- Faster operations")
print("- Cleaner code")
print("- Efficient memory usage")
print("- Useful for large datasets")


# ==========================================
# Task 2: Basic Broadcasting
# ==========================================

print("\n===== Task 2: Basic Broadcasting =====")

arr = np.array([1, 2, 3, 4, 5])

# 1. Add scalar
print("\n1. Add scalar to array")
print(arr + 10)

# 2. Multiply with scalar
print("\n2. Multiply array with scalar")
print(arr * 2)

# 3. Divide by scalar
print("\n3. Divide array by scalar")
print(arr / 2)


# ==========================================
# Task 3: Array Broadcasting
# ==========================================

print("\n===== Task 3: Array Broadcasting =====")

a = np.array([[1], [2], [3]])

b = np.array([10, 20, 30])

# 1. Add compatible arrays
print("\n1. Add two compatible arrays")
print(a + b)

# 2. Multiply arrays
print("\n2. Multiply arrays")
print(a * b)

# 3. Observe shapes
print("\n3. Shape changes")
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)


# ==========================================
# Task 4: Shape Practice
# ==========================================

print("\n===== Task 4: Shape Practice =====")

x = np.array([[1], [2], [3]])

y = np.array([10, 20, 30])

# 1. Print shapes
print("\n1. Print shapes")
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

# 2. Compatible shapes
print("\n2. Compatible shapes")
print("These shapes are compatible for broadcasting.")

print(x + y)

# 3. Incompatible shapes
print("\n3. Incompatible shapes")

a1 = np.array([1, 2, 3])

b1 = np.array([1, 2])

print("Shape of a1:", a1.shape)
print("Shape of b1:", b1.shape)

print("These shapes are incompatible.")
print("Trying this operation gives error:")
print("a1 + b1")


# ==========================================
# Task 5: 2D Broadcasting
# ==========================================

print("\n===== Task 5: 2D Broadcasting =====")

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 1. Add scalar to matrix
print("\n1. Add scalar to matrix")
print(matrix + 100)

# 2. Multiply matrix
print("\n2. Multiply matrix")
print(matrix * 10)

# 3. Normalize matrix values
print("\n3. Normalize matrix values")

normalized = matrix / np.max(matrix)

print(normalized)