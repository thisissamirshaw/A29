#WAP to op a list which contain elements with square of even individual elements
def ext(lt,out=[],i=0):
    if i>=len(lt):
        return out
    if type(lt[i])==int and lt[i]%2==0:
        out.append(lt[i]*lt[i])
    else:
        out.append(lt[i])
    return ext(lt,out,i+1)
print(ext([2,3.5,'Hello',8,7,[1,2]])) 