import matplotlib.pyplot as plt

population=[]
profit=[]

with open('D:\machine-learning-ex1\ex1\ex1data1.txt') as f:
    lines = f.readlines()

for line in lines:
	population.append(float(line.split(",")[0]))
	profit.append(float(line.split(",")[1]))

temp1=1
temp0=1
th1=1
th0=1
alpha=0.01
def calculate():
	global th1
	global th0
	m=len(profit)
	print(m)
	while(1):
		j1=0
		j0=0
		temp1=th1
		temp0=th0
		for i in range(m):
			j0+=(th0+th1*population[i]-profit[i])
			j1+=((th0+th1*population[i]-profit[i])*population[i])
			dj0=j0*alpha/m
			dj1=j1*alpha/m
		print(dj0)
		print(dj1)
		th1-=dj1
		th0-=dj0
		if temp1==th1 and temp0==th0:
			break
	print("\n\n")
	print(th1)
	print(th0)
	x=[i for i in range(25)]
	y=[]
	for i in x:
		y.append(th1*i+th0)
	plt.plot(population,profit,'bx',x,y,'r-')
	plt.xlabel('Profit')
	plt.ylabel('Population')
	plt.show()

def predict(p):
	global th1
	global th0
	print "The profit is ",str(th1*p+th0)

calculate()
while(1):
	pln=int(input("Enter the population and -ve to terminate\n"))
	if(pln>0):
		predict(pln)
	else:
		break