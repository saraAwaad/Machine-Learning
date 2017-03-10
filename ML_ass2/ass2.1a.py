from numpy import loadtxt, where
from pylab import scatter, show, legend, xlabel, ylabel

#load the dataset
data = loadtxt('ex2data1.txt', delimiter=',')

X = data[:, 0:2]
y = data[:, 2]

admit = where(y == 1)
notAdmit = where(y == 0)
scatter(X[admit, 0], X[admit, 1], marker='o', c='b')
scatter(X[notAdmit, 0], X[notAdmit, 1], marker='x', c='r')
xlabel('Exam 1')
ylabel('Exam 2')
legend(['Not Admitted', 'Admitted'])
show()