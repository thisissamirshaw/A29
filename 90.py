#WAP to shift each character of a string by one position in the alphabet.
# For example, 'a' becomes 'b', 'b' becomes 'c', ..., 'y' becomes 'z', and 'z' becomes 'a'.
a='abcstqz'
op='bcdtura'
out=''
for i in a:
    if i!='z':
        out+=chr(ord(i)+1)
    elif i=='z':
        out+='a'
print(out)   