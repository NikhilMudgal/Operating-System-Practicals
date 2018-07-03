import operator
comlist=[]
pl=[]
p=int(input("Enter the number of processes "))
for x in range(1,p+1):
	pl.append(x)
l=[]
print("Enter the burst time and priority of each schedule")
for x in range(p):
	l1=[int(i) for i in input().split()]
	l.append(l1)

for x in range(5):
	l2=[]
	l2.insert(x,pl[x])
	l2.extend(l[x])
	comlist.append(l2)

comlist.sort(key=operator.itemgetter(2))

turn_around=[]
wait_time=[]

wait_time.insert(0,0)
turn_around.insert(0,comlist[0][1])
for i in range(1,len(pl)):
	wait_time.insert(i,wait_time[i-1]+comlist[i-1][1])
	turn_around.insert(i,wait_time[i]+comlist[i][1])
averagtat=0
averagwt=0
for i in range(0,len(pl)):
	averagwt=averagwt+wait_time[i]
	averagtat=averagtat+turn_around[i]
averagwt=float(averagwt)/5
averagwt=float(averagtat)/5
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,len(pl)):
	print(str(pl[i])+"\t\t"+str(comlist[i][1])+"\t\t"+str(wait_time[i])+"\t\t"+str(turn_around[i]))
print("\n")
print("Average Waiting time is: "+str(averagwt))
print("Average Turn Around Time is: "+str(averagtat))
