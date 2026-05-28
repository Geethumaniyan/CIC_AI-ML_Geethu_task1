# =========================================
# AI/ML Internship – Day 31
# Advanced Matplotlib & Subplots
# =========================================

import matplotlib.pyplot as plt
import random

# =========================================
# Task 1: Theory Answers
# =========================================

print("1. What is subplot?")
print("A subplot means displaying multiple graphs inside one figure.")

print("\n2. Why subplots are important?")
print("Subplots help compare datasets, save space, and improve analysis.")

print("\n3. What is figure size?")
print("Figure size controls graph width and height.")

print("\n4. What is legend?")
print("Legend explains graph labels and plotted data.")

print("\n5. What is histogram?")
print("Histogram shows frequency distribution of data.")

# =========================================
# Task 2: Multiple Graphs
# =========================================

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

plt.plot(x, y1, label="Sales")
plt.plot(x, y2, label="Profit")

plt.title("Multiple Line Graphs")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.legend()

plt.show()

# =========================================
# Task 3: Figure Customization
# =========================================

plt.figure(figsize=(8, 5))

plt.plot(x, y1, marker="o", linestyle="--")

plt.title("Customized Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.grid()

plt.show()

# =========================================
# Task 4: Subplot Practice
# =========================================

# Create 2 Subplots
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Graph 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Graph 2")

plt.show()

# Create 4 Subplots
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Plot 1")

plt.subplot(2, 2, 2)
plt.plot(x, y2)
plt.title("Plot 2")

plt.subplot(2, 2, 3)
plt.bar(["A", "B", "C"], [5, 7, 6])
plt.title("Bar Chart")

plt.subplot(2, 2, 4)
plt.scatter([1, 2, 3], [4, 5, 6])
plt.title("Scatter Plot")

plt.tight_layout()

plt.show()

# =========================================
# Task 5: Histogram Practice
# =========================================

# Simple Histogram
data = [10, 20, 20, 30, 40, 40, 40]

plt.hist(data)

plt.title("Simple Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()

# Random Dataset Histogram
random_data = [random.randint(1, 100) for i in range(50)]

plt.hist(random_data)

plt.title("Random Data Histogram")
plt.xlabel("Numbers")
plt.ylabel("Frequency")

plt.show()

# =========================================
# Task 6: Save Graphs
# =========================================

# Save Line Graph
plt.plot(x, y1)

plt.title("Saved Line Graph")

plt.savefig("line_graph.png")

plt.show()

# Save Histogram
plt.hist(random_data)

plt.title("Saved Histogram")

plt.savefig("histogram.png")

plt.show()

# Save Subplot Figure
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title("Left Graph")

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title("Right Graph")

plt.tight_layout()

plt.savefig("subplot_graph.png")

plt.show()

# =========================================
# End of Program
# =========================================