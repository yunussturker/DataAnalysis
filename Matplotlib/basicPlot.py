import matplotlib.pyplot as plt
import numpy as np 

'''
x = np.array([1,2,3,4])
y = x**2

plt.plot(x,y,"o--r")
plt.show()
'''
'''
x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
axs[0,0].plot(x, x)
axs[1,0].plot(x, x**3)
axs[1,1].plot(x, x**4)
axs[0,1].plot(x, x**2)
plt.show()
'''

x = np.linspace(-10,9,20)
y = x**3
z = x**2


myFigure = plt.figure()
'''
cubeAxis = myFigure.add_axes([0.1,0.1,0.8,0.8])
cubeAxis.plot(x,y,"b")
cubeAxis.set_xlabel("X Axis")
cubeAxis.set_ylabel("Y Axis")
cubeAxis.set_title("Cube")

squareAxis = myFigure.add_axes([0.15,0.6,0.25,0.25])
squareAxis.plot(x,y,"y")
squareAxis.set_xlabel("X Axis")
squareAxis.set_ylabel("Y Axis")
squareAxis.set_title("Square")
'''
myAxis = myFigure.add_axes([0.1,0.1,0.8,0.8])
myAxis.plot(x,y,label="Cube")
myAxis.plot(x,z,label="Square")

plt.legend()
plt.show()