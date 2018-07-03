process = []
burst_time = []
arrival_time = []
waiting_time = []
tat = []
ta = 0
wsum = 0
tsum = 0
wavg = 0
btime = 0
sum1 = 0
k = 1
a = int(input("Enter the number of processes : - "))
for i in range(0, a):
    print("Enter the burst time of process : - ")
    n = int(input())
    burst_time.append(n)
    print("Enter the arrival time of the process : - ")
    b = int(input())
    arrival_time.append(b)
arrival_time.sort()
for i in range(0, a):
    process.append(i+1)
for j in range(0, a-1):
    btime = btime + burst_time[j]
    min = burst_time[k]
    for i in range(k, a):
        if btime >= arrival_time[i] and burst_time[i] < min:
            temp1 = process[k-1]
            process[k-1] = process[i]
            process[i-1] = temp1
            temp1 = arrival_time[k-1]
            arrival_time[k-1] = arrival_time[i]
            arrival_time[i] = temp1
            temp1 = burst_time[k-1]
            burst_time[k-1] = burst_time[i]
            burst_time[i] = temp1
    k = k+1

sum1 = sum1+burst_time[0]
waiting_time.append(0)

for i in range(1, a):
    sum1 = sum1 + burst_time[i-1]
    waiting_time.append(sum1 + arrival_time[i])
    wsum = float(wsum) + float(waiting_time[i])

wavg = float(wsum/a)

ta = ta + burst_time[0]
tat.append(ta - arrival_time[0])
for i in range(1, a):
    ta = ta + burst_time[i]
    tat.append(ta - arrival_time[i])
    tsum = float(tsum) + float(tat[i])

tavg = float(tsum/a)


print("Process\t\t Burst Time\t\t Waiting Time\t\t Turn Around Time\t\t Arrival Time")
for i in range(0, a):
    print("\t"+str(process[i])+"\t\t\t"+str(burst_time[i])+"\t\t\t\t"+str(waiting_time[i])+"\t\t\t\t\t"+str(tat[i])+"\t\t\t\t\t\t"+str(arrival_time[i]))
    print("\n")

print("Average waiting time is : - "+str(wavg))
print("Average turn around time is : - "+str(tavg))
