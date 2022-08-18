# arr = [2,1,-7,8]
arr = [-1, 4, 7, 2]
maxx = -1999999999
s = 0

for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            s += arr[k]
            print(arr[k],end = ' ')
        maxx = max(maxx, s)
        s = 0
        print('\n')  
print('Max Sum Subarray = ',maxx)
