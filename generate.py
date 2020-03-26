import numpy as np
import time
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt
def sdvigvpravo(d,bit):
    newmas = [0 for i in range(len(d))]
    for i in range(len(d)):
        newmas[i] = d[i]
    for i in range(bit):
        newmas.append(d[i])
    del newmas[0:bit]
    return newmas
def sdvigvlevo(d,bit):
    newmas = [0 for i in range(len(d))]
    for i in range(len(d)):
        newmas[i] = d[i]
    for i in range(bit):
        newmas.insert(i, d[-bit + i])
        del newmas[-(i + 1)]
    return newmas
def two_in_ten(d,k):
    s = 0
    for i in d:
        s += i * 2 ** k
        k -= 1
    return s
def myrand():
    n = int(time.perf_counter()*10000000000)
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    l = len(b)
    c = int(b)
    d = []
    for i in range(l):
        s = c % 10
        d.append(s)
        c = c // 10
    d.reverse()
    k = l - 1
    bit = l // 4
    newdmas = sdvigvpravo(d, bit)
    newnsprava = two_in_ten(newdmas, k)
    new = sdvigvlevo(d, bit)
    newnsleva = two_in_ten(new, k)
    newc = newnsleva + newnsprava
    return newc
d = []
for i in range(1000):
    d.append(myrand(n)%100)
plt.subplot(2,2,1)
plt.hist(d, bins=50)
plt.subplot(2,2,2)
plt.plot(list(range(1000)),d)
plt.show()
M = np.average(d)
print("Average", M)
D = np.var(d)
print("Dispersion", D)
C = sqrt(D)
print("SredneKvadrat otkl ", C)
