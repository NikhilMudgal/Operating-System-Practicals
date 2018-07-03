max=[[0 for x in range(100)] for y in range(100)]
alloc=[[0 for x in range(100)] for y in range(100)]
need=[[0 for x in range(100)] for y in range(100)]
avail=[[0 for x in range(100)] for y in range(100)]
n=int(input("Enter the no of Processes\t"))
r=int(input("Enter the no of resource instances\t"))

def input():
    print("Enter the Max Matrix\n")
    for i in range(0,n):
        for j in range(0,r):
            max[i][j]=int(input())
    print("Enter the Allocation Matrix\n")
    for i in range(0, n):
       for j in range(0, r):
            alloc[i][j]=int(input())

    print("Enter the available Resources\n")
    for j in range(0,r):
        avail[j]=int(input())


def show():
    print("Process\t Allocation\t Max\t Available\t")
    for i in range(0,n):
        print ("\n")
        print("\nP\t   ",i+1)
        for j in range(0,r):
            print(alloc[i][j])
            print ("\t")
        print("\t")
        for j in range(0,r):
            print ("\n")
            print(max[i][j])
        print("\t");
        if(i==0):
            for j in range(0,r):
                print(avail[j])
                print ("\t")
def cal():
    finish=[0 for i in range(100)]
    temp=0
    need=[[0 for x in range(100)] for y in range(100)]
    flag=1
    c1=0
    k=0
    dead=[0 for i in range(100)]
    safe=[0 for i in range(100)]
    for i in range(0,n):
        finish[i]=0
    for i in range(0,n):
        for j in range(0,r):
            need[i][j]=max[i][j]-alloc[i][j]
    while(flag):
        flag=0
        for i in range(0,n):
            c=0
            for j in range(0,r):
                if((finish[i]==0) and (need[i][j]<=avail[j])):
                    c=c+1
                    if(c==r):
                        for k in range(0,r):
                            avail[k]+=alloc[i][j]
                            finish[i]=1;
                            flag=1;
                        if(finish[i]==1):
                            i=n
    j=0
    flag=0
    for i in range(0,n):
        if(finish[i]==0):
            dead[j]=i
            j=j+1
            flag=1
    if(flag==1):
        print("\n\nSystem is in Deadlock and the Deadlock process are\n")
        for i in range(0,n):
            print("\t",dead[i])
        else:
            print("\nNo Deadlock Occur")
print("********** Deadlock Detection Algo ************\n")
input();
show();
cal();
