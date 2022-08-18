# Problem
#Given an unsorted array A of size N of non-negative integers, find a continuous
#subarray which adds to a given number S.

arr = [1,2,3,7,5]
S = 12
c = 0
d=0
e=0
flag = 0

for i in range(0,len(arr)):
    for j in range(i, len(arr)):
        c += arr[j]
        
        if(c > S):
            break
        
        if(c == S):
            d = i+1
            e = j+1
            flag = 1
            break       
                        
    if(flag == 1):
        break
    c = 0        

if(d == e):
    print(d)
else:
    print(d,' ',e)
        
































