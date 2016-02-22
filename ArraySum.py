
       
n = int(input("enter size of array"))
s = raw_input("enter values")
a = [ int(i) for i in s.split()]

for i in range (0,n):
    print a[i]
    
print sum(a)