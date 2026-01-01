#WAP to print all uppercase and at even place and 
# ascii val is deisivible by 3 and print the count also
def ex_up():
    a=input("Enter a collection")
    out=''
    count=0
    for i in range(1,len(a)):
        if 'A'<=a[i]<='Z' and i%2==0 and ord(a[i])%3==0:
            count+=1
            out+=a[i]
    return out,count
print(ex_up())        
