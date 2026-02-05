# a='python star'
# Op={python:[python,6], star:[star,4]}
# Without using len or count or any other built in function
a='python star'.split()
print(a)
out={}
i=0
while i<len(a):
    out[a[i]]=[[a[i]]+[len(a[i])]]
    i+=1
print(out)   



# a='python star'
# Op={python:[python,6], star:[star,4]}
# Without using len or count or any other built in function

a='python star'.split()
out={}
for i in a:
    count=0
    for j in i:
        count+=1
    out[i]=[i,count]
print(out)

#3rd Process

a='python star'.split()
result={}
index=0
while index < len(a):
    word = a[index]
    count = 0
    for char in word:
        count += 1
    result[word] = [word, count]
    index += 1
print(result)




