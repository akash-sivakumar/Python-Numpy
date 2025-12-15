import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)

b = a.reshape(2,3)
print(b)

c = b.flatten()
print(c)

d = b.ravel()
print(d)

e = b.transpose ()
print(e)

print(b.shape)
print(b.T.shape)