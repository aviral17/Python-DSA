arr = [-20,50,68,4,32,1,4,8]
maxx = -1999999

for i in range(1,len(arr)):
    k = i-1
    maxx = max(maxx, arr[i])

print(maxx)    
