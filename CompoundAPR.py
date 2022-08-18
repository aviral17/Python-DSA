n = int(input("Enter Initial Amount: "))
z = n
x = float(input("Enter APR interest percentage: "))
days = int(input("Enter the no. of days upto which U want to check Ur Total money with Compound interest: "))

arr = []

if not arr:
    c = n*(x/100)
    daily = c/365
    n = n+daily
    arr.append(n)
    
for i in range(1, days):
    n = arr[i-1]
    c = n*(x/100)
    daily = c/365
    n = n+daily
    arr.append(n)

print("Total Money after ",days," days with Compound interest will be ", arr[len(arr)-1])
print("Total Interest Earned in ",days," days = ", arr[len(arr)-1] - z)
        
        




