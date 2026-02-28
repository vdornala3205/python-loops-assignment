# Q:1
# Question: Temperature and Data Processing 

# Task 1: Create an Array and Basic Math

import numpy as np

# 1. Create the NumPy array
temps_celsius = np.array([22, 25, 28, 24, 26])

# 2. Convert to Fahrenheit
temps_fahrenheit = temps_celsius * 1.8 + 32

# 3. Calculate the average
avg_fahrenheit = np.mean(temps_fahrenheit)

print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")
print(f"Average Fahrenheit: {round(avg_fahrenheit, 1)}")

print(f"*******************************************************************")

# Task 2: Array Shape and Statistics

#1. Initializing the Array
scores = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

# 2. Statistics
shape = scores.shape
total_elements = scores.size
high_score = np.max(scores)
low_score = np.min(scores)
score_range = high_score - low_score

print(f"Shape: {shape}")
print(f"Total elements: {total_elements}")
print(f"Highest score: {high_score}")
print(f"Lowest score: {low_score}")
print(f"Range: {score_range}")

print(f"*******************************************************************")

# Task 3: Performance Comparison

import time

# 1. Create data structures i.e. NumPy Array & Python List
np_arr = np.arange(1, 50001)
py_list = list(range(1, 50001))

# 2. Measure Time NumPy
start_np = time.time()
np_sum = np.sum(np_arr)
end_np = time.time()
np_time = end_np - start_np

# 3. Measure Time Python List
start_py = time.time()
py_sum = sum(py_list)
end_py = time.time()
py_time = end_py - start_py

# 4. Measure Speed NumPy vs Python
times_faster = py_time / np_time

# 5. Output
print(f"NumPy sum: {np_sum}")
print(f"Python sum: {py_sum}")
print(f"NumPy time: {np_time:.4f} seconds")
print(f"Python time: {py_time:.4f} seconds")
print(f"NumPy is {round(times_faster, 1)}x faster")
