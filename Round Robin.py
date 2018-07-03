queue = []
total_time = 0
total_tattime=0
total_tattime=0
n = int(input('Enter the total no of processes: '))
x = int(input('Enter the Quantum: '))
for i in range(n):
    queue.append([])
    queue[i].append(input('Enter process name: '))
    queue[i].append(int(input('Enter process arrival time: ')))
    queue[i].append(int(input('Enter process burst time: ')))   
queue.sort(key = lambda queue:queue[1])
print ('Table:\n')
for i in range(n):
    queue.append([])  
    total_time += queue[i][2]
    
print ('ProcessName\tArrivalTime\tBurstTime\t')
for i in range(n):
    print (str(queue[i][0])+'\t\t'+str(queue[i][1])+'\t\t'+str(queue[i][2]))

print ('Gantt Chart:\n')
a=queue[0][1]
i=0
j=1
total_time += a
while True:
    
    print (a)
    if(queue[i][2]>=x):
        print (str(queue[i][0]))
        queue[i][2] -= x
        a+=x
    elif(queue[i][2]<x):
        print (str(queue[i][0]))
        a += queue[i][2]
        queue[i][2]=0
    i = i+1
    if(i>=n):
        i=0
    if a==total_time:
        break
print(a)
