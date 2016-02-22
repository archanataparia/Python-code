#wrong code
n = int(input())
l1 = ["#"]*1
for i in range(n):
    for j in range(n,i,-1):
        print " ",
    print l1[0]*i
    