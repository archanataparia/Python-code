def cbp(s):
    l= len(s)
    stack = []
    for i in range(0,l):
        if ((s[i] =='(') or (s[i]=='{') or (s[i] == '[')):
            stack.append(s[i])
            #print s[i]
        elif ((s[i] ==')') or (s[i]=='}') or (s[i] == ']')):
            if (len(stack)==0 ):
                print "not valid"
                return
            else:
                stack.pop()
        else:
            print "nthng"
    print "valid"
    
s= str(raw_input("enter values\n"))
cbp(s)