#WAP to do the following output
#a='nitin is ava ata boy'
#op='nitin ava ata'
#take out the palindrome words in a string
a='nitin is ava ata boy'.split()
op='nitin ava ata'
i=0
out=''
while i<len(a):
    if a[i]==a[i][::-1]: #it is very crucial for me the see what is a[i][::-1]means and a[][]
        out+=a[i]
        out+=' '
    i+=1
print(out)        
    