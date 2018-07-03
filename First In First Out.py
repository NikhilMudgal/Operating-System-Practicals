a = [1, 2, 3, 4, 2, 1, 5, 6, 2, 1, 2, 3, 7, 6, 3, 2, 1, 2, 3, 6]
n = len(a)
m = int(raw_input("Enter the frame size"))
def __fifo():
    global a, n, m
    f = -1
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if (page[j] == a[i]):
                flag = 1
                break

        if flag == 0:
            f = (f + 1) % m
            page[f] = a[i]
            page_faults += 1
            print "\n%d ->" % (a[i]),
            for j in range(m):
                if page[j] != -1:
                    print page[j],
                else:
                    print "-",
        else:
            print "\n%d -> No Page Fault" % (a[i]),

    print "\n Total page faults : %d." % (page_faults)

print "\n SIMULATION OF PAGE REPLACEMENT ALGORITHM"
print " 1. FIFO."
__fifo()
