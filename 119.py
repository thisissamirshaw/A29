#WAP to op the len of words in key value pair
#{'Power': 5, 'Star': 4}
def coun():
    a="Power Star".split()
    b={}
    for i in a:
        coun_t=0
        for j in i:
            coun_t+=1
        b[i]=coun_t
    return b
print(coun())