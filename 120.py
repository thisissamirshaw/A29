# WAF to print [(1,1),("Hello",5),([1,2],2),(3.8,1),(3+5j,1)] 
# from a=[1,"Hello",[1,2],3.8,3+5j]
def maniPulate():
    b=[]
    a=[1,"Hello",[1,2],3.8,3+5j]
    for item in a:
        if type(item)==str or type(item)==list:
            b.append((item,len(item)))
        else:
            b.append((item,1))
    print(b)
#maniPulate()