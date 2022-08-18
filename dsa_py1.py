n = int(input("Enter no.: "))
print('\n')

#Best Alternate method to solve this
for i in range(1,n+1):
    for j in range(1,i+1):
        if((i+j)%2 == 0):
            print('1',end=' ')
        else:
            print('0', end=' ')
    print('\n') 


#**************************#
for i in range(1,n+1):
    if((i%2)==0):
        for j in range(1,i+1):
            if((j%2)!=0):
                print('0',end=' ')
            else:
                print('1',end=' ')
        print('\n')
    else:
        for j in range(1,i+1):
            if((j%2)!=0):
                print('1',end=' ')
            else:
                print('0',end=' ')
        print('\n')
