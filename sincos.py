# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:55:08 2019

@author: gaura
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('Values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('sin and cos function for one period')
plt.legend('sin(x)', 'cos(x)')
plt.show()
