#WAP to count alphabets in a word
a='abaabcdabc'
out={} #the default value of dict
i=0
while i<len(a):
    out[a[i]]=a.count(a[i]) #this is the process how you could make a dict
    i+=1
print(out)    
# print(a.count('a'))
# print(a.count('b'))
# print(a.count('c'))
# print(a.count('d'))
# print(a.count('z'))
#i=0