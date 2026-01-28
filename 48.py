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
print(out+str(count))
#alternate
#out=out+(str)count     
#print(out+str(len(out)))