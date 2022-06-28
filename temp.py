import numpy as np
a=np.array([1,2,3,4,5])
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b)

print(b.shape)

a=range(10)
print(a)

a=np.arange(10,20,2)
print(a)
b=np.arange(20)
print(b)

t=np.linspace(1, 10,num=4)
print(t)

s=np.linspace(1, 10,num=4,endpoint=False,retstep=True)
print(s)

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b=a.reshape((3,4))
print(b)
c=a.reshape((2,-1))
print(c)
print(b[1:3,1:3])
print(b[1: ,2: ])