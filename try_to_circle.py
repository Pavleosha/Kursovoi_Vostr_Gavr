import numpy as np
import matplotlib.pyplot as plt

T = [1, 10, 20, 30, 40, 50, 50]
R = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]



def rtpairs(r, n):

    for i in range(len(r)):
       for j in range(n[i]):
        yield r[i], j*(np.pi /(2 * n[i]))

for r, t in rtpairs(R, T):
    plt.plot(r * np.cos(t), r * np.sin(t), 'bo')
plt.show()