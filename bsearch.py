import sys
import math

def binarySearch(alist, item):
    location = binarysearch(alist, item, 0, len(alist) - 1)
    # easier for programmer to use indicies than to manage new arrays
    return location


def binarysearch(alist, item, min, max):
 	# Insert Code Here
  
   
    if item >= alist[min]:
 
        mid = min + (max - min)/2
 
        if alist[mid] == item:
            return mid
         
        #element in mid > item - recurse left half array
        elif alist[mid] > item:
            return binarysearch(alist, item, min, mid-1)
 
        else:
            return binarysearch(alist, item, mid+1, max)
 
    else:
        return -1
  

#Read input
[t, n] = [int(x) for x in sys.stdin.readline().split()]
alist = [int(x) for x in sys.stdin.readline().split()]
index = binarySearch(alist, t)
print index
