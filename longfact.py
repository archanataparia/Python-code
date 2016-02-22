#long factorial
n = long(raw_input("enter number"))
#print n
f=1
while(n>0):
    f*=n
    n-=1
print f