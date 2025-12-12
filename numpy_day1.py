import numpy as np
a = np.array([10,20,30,40,50])
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)

print("dimension:",a.ndim)
print("shape:",b.shape)
print("data type:",a.dtype)
print("size:",a.size)

c= np.arange(0,21)
print(c)

print(np.zeros(5))
print(np.ones(5))