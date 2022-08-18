# we must not swap the elements with each other, not good for space complexity
arr = [12,45,23,51,19,8]

for i in range(1,len(arr)):
    j = i
    while((arr[j-1] > arr[j]) and j>0):
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j-=1
        
print(arr)

