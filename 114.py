#WAP to print {'P':['Python','Programming'],'i':['is'],'l':['language']} from 
# a= "Python is Programming language"
def extract():
    a="Python is Programming language".split()
    out={}
    for i in a:
        if i[0] not in out:
            out[i[0]]=[i]
        else:
            out[i[0]]+=[i]
    return out
print(extract())        