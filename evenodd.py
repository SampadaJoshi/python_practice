n=eval(input('Enter any number:'))

if n>0:
    if n%2==0:
        print('{} is positive and even number'.format(n))
    else:
        print('{} is positive and odd number'.format(n))
elif n<0:
    if n%2==0:
        print('{} is negative and even number'.format(n))
     else:
        print('{} is negative and odd number'.format(n))
    
