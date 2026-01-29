#WAP sum of 10 natural numbers by resursion
def sum(n):
    summ=0
    if n==1:
        return summ+1
    return summ+n+sum(n-1)
print(sum(10))