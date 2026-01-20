#i th arg and without written vals
#WAP to create a tuple with elements and their lengths/count
a=[1,'Hello',[1,2],3.8,3+5j]
op=[(1,1),('Hello',5),([1,2],2),(3.8,1),(3+5j,1)]
def tupp(a):
    out=[]
    for i in a:
        if type(i) in (int,float,complex):
            out.append((i,1))
        elif type(i) in (str,list):
            out.append((i,len(i)))
    print(out)
tupp(a)
          



