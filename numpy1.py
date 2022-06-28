import numpy as np
t=np.arange(1,41).reshape(10,4)
print(t)
e=t.reshape(1,-1)
for i in range(0,35,4):
    print(e[0,i:i+8])
