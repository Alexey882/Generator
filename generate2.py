import time
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
def generate(seed):
    seed = (8253729 * seed + 2396403)
    return seed % 69069
d = []
for i in range(1000):
    seed = int(time.perf_counter()*100000000)
    d.append(generate(seed)%100)
    plt.subplot(2,2,1)
plt.plot(list(range(1000)), d)
plt.subplot(2,2,2)
plt.hist(d, bins = 50)
plt.show()
M = np.average(d)
print("Average", M)
D = np.var(d)
print("Dispersion", D)
C = sqrt(D)
print("SredneKvadrat otkl ", C)