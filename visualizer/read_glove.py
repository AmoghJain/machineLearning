def findMax(ll):
	ns=[]
	for i in ll:
		for j in i.split(" ")[1:]:
			ns.append(float(j))
	return max(ns)

def findMin(ll):
	ns=[]
	for i in ll:
		for j in i.split(" ")[1:]:
			ns.append(float(j))
	return min(ns)

words=["drink ","bike "]
results = []
with open("glove.6B.100d.txt","r")as data:
	lines=data.readlines()

completeStr=""

for i in range(100):
	completeStr+=str(i)+","
completeStr+=str(100)
completeStr+="\n"


ll=[]
for word in words:
	oline=" "
	for line in lines:	
		if line.startswith(word):
			ll.append(line)

lmax=findMax(ll)
lmin=findMin(ll)



for word in words:
	oline=" "
	for line in lines:	
		if line.startswith(word):
			ls=line.split(" ")
			oline+=ls[0]+","
			for s in ls[1:len(ls)-1]:
				sd=(float(s)-lmin)/(lmax-lmin)
				oline+=str(sd)+","
			oline+=str((float(ls[len(s)-1])-lmin)/(lmax-lmin))
	completeStr+=oline+"\n"

print(completeStr)

with open("/home/amogh/Desktop/visualizer/csv2radar.html","r") as csvr:
	cr=csvr.read()

asd=cr.replace("change_me",completeStr)

with open("/home/amogh/Desktop/visualizer/csv2radar2.html","w") as csvw:
	csvw.write(asd)


