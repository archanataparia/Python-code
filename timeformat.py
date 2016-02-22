s = raw_input()
h=0
if ('PM' in s):
    h = s[0:2]
    if (int(h) < 12):
        h1 = int(h) + 12
        print str(h1) +s[2:len(s)-2]
    else:
        print str(h) +s[2:len(s)-2]   
elif('AM' in s):
    h = s[0:2]
    if (int(h) == 12):
        h = "00"
        print str(h) +s[2:len(s)-2]
    else:
        print s[0:len(s)-2]


