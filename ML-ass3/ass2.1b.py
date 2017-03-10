import math

def sigmoid(x,theta):
	return 1 / (1 + math.exp(-1*theta*x))
#cost function =j=(1/2m)*sum((h(xi)-yi)^2) from i to m where m is no. of data samples
#h(x)=theta0 + theta1* x
#initilization theta0=0 ,i=1
def calculate_costFunction(x,y,m,theta):
	J = 0
	sum=0
	grad=0
	
	for i in range (0,m):
		X=float(x[i])
		Y=float(y[i])
		hi = sigmoid(X,theta)
		#i should prevent hi=0 or =1 
		sum= sum+ (-1*Y* math.log(hi))-((1-Y)*math.log(1-hi))
		grad=X*(hi - Y)
	J=sum/m
	grad = grad/m;

	print("cost = ",J," Gradient= ",grad)
	return

#read samples from the file
with open("ex2data1.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y = [row.split(',')[1] for row in data]
#m is no. of training samples
m =len(y)
print ("no of samples ",m)
#calculate J(0,1)
calculate_costFunction(x,y,m,0.2)