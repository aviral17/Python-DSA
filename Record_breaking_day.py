arr = [1,2,0,7,0,2,2,12]

l = 0
mx = arr[0]
last = len(arr) - 1

for i in range(1, len(arr)):
        if((i+1) == len(arr)):
            mx = max(mx, arr[i])
            if(mx == arr[last]):
               l+=1
               print(mx)
            break
        
        if((arr[i] > mx) and arr[i] > arr[i+1]):
            mx = max(mx, arr[i])
            l+=1
            print(mx)

print('Total No. of Record Breaking Days are: ', l)
