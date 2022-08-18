n = int(input("Enter any no.: "))
print('\n')
b = n+1
c=(n*2) + 1
d=n*2

for i in range(1,b):
    for j in range(1,c):
        if(j<=i or j>(n*2)-i):
            print('*',end= ' ')
        else:
            print(' ',end = ' ')
    print('\n')
for i in range(n,0,-1):
            for j in range(1,c):
                if(j<=i or j>(n*2)-i):
                    print('*',end= ' ')
                else:
                    print(' ',end = ' ')
            print('\n')    
        
      
