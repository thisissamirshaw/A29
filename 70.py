#WAP a='aaabcbb' and op='a3b1c1b2'
#a='aaabcbb'
#out='' 
#i=0
#c=1
#while i<len(a):
#    if(a[i]=a[i+1]):
#        out+=a[i]+str(c+1)
#elif:     out+=a[i]+str(a.count(a[i])) #this is the process how you could make a dict
#    i+=1
#print(out) 

# Correct implementation with single loop
# a = 'aaabcbb'
# out = ''
# if a:
#     current = a[0]
#     count = 1
#     for i in range(1, len(a)):
#         if a[i] == current:
#             count += 1
#         else:
#             out += current + str(count)
#             current = a[i]
#             count = 1
#     out += current + str(count)
# print(out)

# Implementation with one while loop
a = 'aaabcbb'
out = ''
if a:
    current = a[0]
    count = 1
    i = 1
    while i < len(a):
        if a[i] == current:
            count += 1
        else:
            out += current + str(count)
            current = a[i]
            count = 1
        i += 1
    out += current + str(count)
print(out)

# Previous implementation with two loops
# a = 'aaabcbb'
# out = ''
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     count = j - i
#     out += a[i] + str(count)
#     i = j
# print(out)
# a = 'aaabcbb'
# out = ''
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     count = j - i
#     out += a[i] + str(count)
#     i = j
# print(out) 
    