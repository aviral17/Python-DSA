n = int(input('Please enter ur initial amount:  '))
x = float(input('Enter BUY price:  '))

#y = n/x  x will be same, n will change
#z = 0.80*y
#j = int(input('Please enter increment percentage in number:  '))
print('\n')
#inc = j/100
for i in range(30):
    y = n/x
    z = 0.80*y
    n = n+z
    print('Amount on ',i+1,' day is Rs ', int(n),'\n')

