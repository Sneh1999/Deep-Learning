import numpy as np
import time
a = np.array([1, 2, 3, 4])
print(a)

import time 

a = [15,2]
b = [13,5]

tic = time.time()
c = np.dot(a,b)

print(c)

c=0

for i in range(0,2):
    c+=a[i]*b[i]

print(c)

