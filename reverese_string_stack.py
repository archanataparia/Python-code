class Stack:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return len(self.item) == 0
    def pop(self):
        return self.item.pop()
    def push(self,item):
        return self.item.append(item)
        
s = str(raw_input("Enter string to reverse\n"))
l= len(s)
stack= Stack()
r =[]
#reverse = []
for i in range(0,l):
    stack.push(s[i])
    #print stack

#for i in range(0,l):
 #   r = stack.pop()
  #  reverse.append(r)
#print reverse

while not stack.isEmpty():
       r += stack.pop(),
       
print ("".join(r))
       
