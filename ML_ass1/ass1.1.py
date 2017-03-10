import matplotlib.pyplot as plt
import numpy as np


with open("ex1data1.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y = [row.split(',')[1] for row in data]

fig = plt.figure()

plt.plot(x,y,marker='o',linestyle='None', c='r', label='the data')
#plt.plot(x,y,marker='o',linestyle='--', c='r', label='the data')


plt.xlabel('population')
plt.ylabel('profit ')
plt.title('About as simple as it gets, folks')


plt.grid(True)
plt.legend()
plt.savefig("ass1.png")

plt.show()




