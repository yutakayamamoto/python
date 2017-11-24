from math import exp
import numpy as np
import matplotlib.pyplot as plt

print(exp(0))
print(exp(1))


# evenly sampled time at 200ms intervals
x = np.arange(0., 150., 1)
y = np.exp(-x)
plt.plot(x,y)
plt.show()
