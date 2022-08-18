# Arrays Challenge - Smallest Positive Missing Number
# (Amazon, Samsung, Snapdeal, Accolite)

arr = [0,-9,1,3,-4,5]
c = 0
d=0

for a in range(len(arr)):
    if(arr[a] < 0):
        pass
    else:
        if c in arr:
            c+=1
            pass
        else:
            d=c
            break
print(d)           
