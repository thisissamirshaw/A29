# #ASCII Lecture
# print(chr(85))
# print(ord('85'))


#WAP to convert lowercase to uppercase
a='haihello'
op='HAIHELLO'
out=''
i=0
while i<len(a):
    if 'a'<=a[i]<='z':
        out+=chr(ord(a[i])-32)
    i+=1
print(out)        