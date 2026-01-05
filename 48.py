#WAP to extract uppercase and total count
a=input("enter a str")
out=''
i=0
count=0
while i<len(a):
    if 'A'<=a[i]<='Z':
        out+=a[i]
        count+=1
    i+=1 
#out=out+(str)count     
#0print(out+str(len(out)))
print(out+str(count))