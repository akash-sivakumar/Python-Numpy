import numpy as np
a = np.array([10,20,30,40,50,60,70])
print(a[0])   # first element.
print(a[-1])  # last element.
print(a[2:5]) # slice from index 2 to 4.
print(a[:4])  # first 4 elements.
print(a[::-1])# reverse array.

b = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(b[0,1]) # 10
print(b[2,2]) # 45
print(b[1])   # entire row 1 (2nd row).   
print(b[:,1]) # entire column 1 (2nd column).

print(b[0:2,1:3]) # sub-array from rows 0-1 and columns 1-2.

print(b[::-1]) # reverse rows

c = np.arange(1,21)
print(c[::2])  # every second element.
print(c[1::2]) # every second element starting from index 1.

d = np.array([3,6,9,12,15,18,21])
print(d[(d>10) & (d%3==0)]) # elements greater than 10 and divisible by 3.