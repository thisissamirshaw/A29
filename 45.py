# WAP to extract all the upppercase
#  alphabet from a given string
a=input("enter a str")
out=''
i=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        out+=a[i]
    i+=1    
print(out)


#one by one
a=input("enter a str")
out=''
i=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        print(a[i])
    i+=1    

