import numpy as np
a = np.array([10,20,30,40,50]) # In this we created the arr and then we printing.
print(a)

b = np.array([[1,2,3],[4,5,6]]) # In this also we created the arr name a variable is b and then printing it.
print(b)

print("dimension:",a.ndim) #This is used to check the dimension of the arr.
print("shape:",b.shape)    #This will be used to check the shape of the arr.
print("data type:",a.dtype) #This is used to check the data type of the arr.
print("size:",a.size)       #This will be used to check the size of the arr.

c= np.arange(0,21) #In this we created the array to 0 to 20 and then printing it.
print(c)

print(np.zeros(5)) # In this we printing five 5 zeros from the array.

print(np.ones(5)) #In this we are printing one for five times from the array.
