#WAP 
a=[1,'Hello',[1,2],3.8,3+5j]
op=[(1,1),('Hello',5),([1,2],2),(3.8,1),(3+5j,1)]

def tupp(a):
    out=[]
    for i in a:
        if type(i)==int:
            out.append((i,1))
        elif type(i)==str:
            out.append((i,len(i)))
        elif type(i)==list:
            out.append((i,len(i)))
        elif type(i)==float:
            out.append((i,1))
        elif type(i)==complex:
            out.append((i,1))
    print(out) 
           



