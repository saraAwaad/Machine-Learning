


import matplotlib.pyplot as plt
import numpy as np

#cost function =j=(1/2m)*sum((h(xi)-yi)^2) from i to m where m is no. of data samples
#h(x)=theta0 + theta1* x
#initilization theta0=0 ,i=1
from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt

def calculate_costFunction(x,y,m,theta0,theta1):
	a=1/(2*m)
	sum=0
	for i in range (0,m):
		hx=theta0+theta1*float(x[i])
		er=pow((hx-float(y[i])),2)
		#print("er ",er)
		sum=sum+er		
	j=a*sum
	print("cost = ",j)
	return j

#get samples	
with open("ex1data1.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y = [row.split(',')[1] for row in data]

#m is no. of training samples
m =len(y)
print ("no of samples ",m)
#calculate J(0,1)

theta0 = arange(-3.0,3.0,0.1)
theta1 = arange(-3.0,3.0,0.1)
X,Y = meshgrid(theta0, theta1) # grid of point
Z = calculate_costFunction(x,y,m,X, Y) # evaluation of the function on the grid
#plot surface
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.xlabel('theta0')
plt.ylabel('theta1 ')
#Draw contour
plt.figure()
CS = plt.contour(X, Y, Z, 6,
                 linewidths=np.arange(.5, 4, .5),
                 colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5')
                 )
plt.clabel(CS, fontsize=9, inline=1)
plt.title('Cost Function J')
plt.xlabel('theta0')
plt.ylabel('theta1 ')
plt.show()

