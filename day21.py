# AI/ML Internship – Day 21
# Module 4: NumPy (Reshaping & Array Manipulation)

import numpy as np

print("===== Task 1: Theory Examples =====")

# 1. Reshape
print("\n1. Reshape Example")
arr = np.array([1, 2, 3, 4, 5, 6])

reshaped_2d = arr.reshape(2, 3)
print(reshaped_2d)

# 2. Reshape to 3D
print("\n2. Reshape to 3D")
reshaped_3d = arr.reshape(1, 2, 3)
print(reshaped_3d)

# 3. Invalid Reshape
print("\n3. Invalid Reshape")

try:
    invalid = arr.reshape(4, 2)
    print(invalid)
except ValueError as e:
    print("Error:", e)

# 4. Flatten
print("\n4. Flatten Array")

arr2 = np.array([[1, 2],
                 [3, 4]])

flat = arr2.flatten()
print(flat)

# 5. Ravel
print("\n5. Ravel Array")

ravel_arr = arr2.ravel()
print(ravel_arr)

# 6. Compare flatten and ravel
print("\n6. Compare flatten() and ravel()")

print("Flatten Output:", arr2.flatten())
print("Ravel Output:", arr2.ravel())

# 7. Transpose
print("\n7. Transpose Matrix")

print(arr2.T)

# Verify rows and columns
print("\nOriginal Shape:", arr2.shape)
print("Transpose Shape:", arr2.T.shape)

# 8. Vertical Stacking
print("\n8. Vertical Stack")

a = np.array([1, 2])
b = np.array([3, 4])

print(np.vstack((a, b)))

# 9. Horizontal Stacking
print("\n9. Horizontal Stack")

print(np.hstack((a, b)))

# 10. Combine Arrays
print("\n10. Combine Arrays")

x = np.array([10, 20])
y = np.array([30, 40])

combined = np.hstack((x, y))
print(combined)

# 11. Split Array
print("\n11. Split Array")

arr3 = np.array([1, 2, 3, 4])

split_arr = np.split(arr3, 2)
print(split_arr)

# 12. Split Rows
print("\n12. Split Rows")

arr4 = np.array([[1, 2],
                 [3, 4]])

split_rows = np.vsplit(arr4, 2)
print(split_rows)

print("\n===== Program Completed =====")