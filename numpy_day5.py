import numpy as np
print(np.random.rand())  # Random float:  0.0 <= x < 1.0

print(np.random.rand(5))  # 1D array of 5 random floats
 
print(np.random.rand(3,2)) # 2D array (3x2) of random floats

print(np.random.randint(1, 101, size=5)) # 1D array of 5 random integers between 1 and 100

np .random.seed(42)  # Set seed for reproducibility
print(np.random.randint(1, 10, 5)) # 1D array of 5 random integers between 1 and 9

a = np.array([1, 2, 3, 4, 5])
np.random.shuffle(a)  # Shuffle the array in place
print(a)
