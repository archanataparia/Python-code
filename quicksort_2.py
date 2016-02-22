'''
Created on Oct 19, 2015

@author: srathi
'''

def partition(ar,start,end):
    swap = 0;
    pivot = ar[end]
    pindex = start
    for i in range(start,end):
        if  ar[i] <= pivot:
            temp = ar[i]
            ar[i] = ar[pindex]
            ar[pindex] = temp
            pindex += 1;
            swap += 1
    temp = ar[end]
    ar[end] = ar[pindex]
    ar[pindex] = temp
    swap += 1
    print swap
    return pindex
    
def quicksort(ar,start,end):
    swap = 0
    if start < end:
        pindex = partition(ar,start,end)
        #swap += swap
        print " ".join(map(str,ar))
        quicksort(ar, start, pindex -1)
        quicksort(ar, pindex + 1,end)
    #print swap
    return ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quicksort(ar,0,len(ar) -1)

