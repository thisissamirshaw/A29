#WAP to print the special character from any email id
a='samirshaw3525@gmail.com'
i=0
out=''
while i<len(a):
    #if(a[i] in '@!#$%^&*()')
    if not ('A'<=a[i]<='Z'or 'a'<=a[i]<='z'or'0'<=a[i]<='9'):
        out+=a[i]
    i+=1
print(out)        


