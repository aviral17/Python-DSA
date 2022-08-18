n = int(input('Enter any no.: '))
print('n\n')

for i in range(1,n+1):
    s = n-i
    d = s+1
    for j in range(1,d):
        if(s>0):
            print(' ',end=' ')
    for b in range(i,0,-1):
        print(b,end=' ')
    for c in range(2,i+1):
        print(c,end=' ')
    print('\n')         
