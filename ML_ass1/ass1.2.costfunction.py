  
#cost function =j=(1/2m)*sum((h(xi)-yi)^2) from i to m where m is no. of data samples
#h(x)=theta0 + theta1* x
#initilization theta0=0 ,i=1
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
	return



#read samples from the file
with open("ex1data1.txt") as f:
#with open("studentGrades.txt") as f:
    data = f.read()

data = data.split('\n')

x = [row.split(',')[0] for row in data]
y = [row.split(',')[1] for row in data]
#m is no. of training samples
m =len(y)
print ("no of samples ",m)
#calculate J(0,1)
calculate_costFunction(x,y,m,0.0,1.0)

