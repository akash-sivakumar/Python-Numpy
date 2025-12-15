import numpy as np
a = np.array([10,20,30,40])
print(a+5)     # Adding 5 to each element
print(a-5)     # Subtracting 5 from each element
print(a*2)     # Multiplying each element by 2
print(a/2)     # Dividing each element by 2
print(a//2)    # Floor division of each element by 2

b = np.array([5,10,15,20,25])

print("sum:",np.sum(b))   # Sum of all elements
print("mean:",np.mean(b))  # Mean of all elements
print("max:",np.max(b))   # Maximum element
print("min:",np.min(b))   # Minimum element
print("std:",np.std(b))   # Standard deviation
print("var:",np.var(b))   # Variance
print("avg:",np.average(b))  # Average of all elements

c = np.array([[10,20,30],[40,50,60],[70,80,90]])    # 2D array
print(c)

print("column-wise sum:",np.sum(c,axis=0)) # Sum along columns
print("row-wise sum:",np.sum(c,axis=1))    # Sum along rows

print("column-wise mean:",np.mean(c,axis=0))   # Mean along columns
print("row-wise mean:",np.mean(c,axis=1))    # Mean along rows
 
print("column-wise max:",np.max(c,axis=0))  # Max along columns
print("row-wise max:",np.max(c,axis=1))     # Max along rows

d = np.array([12,5,30,7,45,20])         # 1D array basic filtering
print(d[d>15])

e = np.array([10,15,20,25,30,35,40])     # 1D array with multiple conditions
print(e[(e>20) & (e%2==0)])