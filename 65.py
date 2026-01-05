#WAP to check the string is palindrome or not using while loop and not any in-bulit function and also not [::-1], no nested loops.
a='nitin'
i=len(a)-1
out=''
while i>=0:
    out+=a[i]
    i-=1
    if out ==a:
        print('palin')
    else:
        print('not palin')

    
