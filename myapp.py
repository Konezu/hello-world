#my first python

import math
import numpy as np
from matplotlib import pyplot as plt

pi = math.pi

x = np.linspace(0,2*pi,100)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_sin2 = y_sin + 2

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(x,y_sin,label="sin")
ax1.plot(x,y_sin2,label="sin2")
ax1.legend()

ax2 = fig.add_subplot(212)
ax2.plot(x,y_cos)
plt.show()

'''
#plot in graph
plt.plot(x,y_sin,label="sin")
plt.plot(x,y_cos,label="cox")
plt.plot(x,y_sin2,label="sin2")
#graph title,axis
plt.title("sin and cos graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
#graph show
plt.show()
'''
