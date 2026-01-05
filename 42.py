#WAP to reverse a number without taking it as a str
a=143
op=341
rev=0
while a!=0:
    ld=a%10
    rev=rev*10+ld
    a=a//10
print(rev)    
    