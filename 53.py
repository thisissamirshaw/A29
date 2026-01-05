#WAP to extract only the palindrome integers from a list and print in a new list
a=[11,121,97,'hello',3.5,12]
i=0
out=[]
while i<len(a):
    if(type(a[i])==int):
        s=str(a[i])
        if(s==s[::-1]):
            out.append(a[i])
    i+=1
print(out)
#---------OR----------
#if(type(a[i]==int and str(a[i]==str(a[i][::-1]))))