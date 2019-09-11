@author: gaura
"""


import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
t = np.tan(x)
plt.plot(x,y,x,z,x,t)
plt.xlabel('Values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('sin and cos function for one period')
plt.legend('sin(x)', 'cos(x)')
plt.ylabel('sin(x), cos(x) and tan(x)')
plt.title('sin,cos and tan function for one period')
plt.legend('sin(x)', 'cos(x)', 'tan(x)')
plt.show()
