arr = [10,7,4,1,-2,6,8,10,11]
maxx = 1
diff = 0
di = 0
l = 0

for i in range(1,len(arr)):
    diff = arr[i] - arr[i-1]
    if((i-1) == 0):
        di = diff
        l+=1
        
    else:
        if(di == diff):
            l+=1
            maxx = max(maxx, l)
        else:
            l = 1
            di = diff
     
print(maxx+1) 








            
