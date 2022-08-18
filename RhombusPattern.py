n = int(input('Enter no.: '))
print('\n')


for i in range(1,n+1):
    s = n-i
    for j in range(1, s+1):
        print(' ',end=' ')
    for k in range(1,n+1):
        print('*',end=' ')
    print('\n')    
        
