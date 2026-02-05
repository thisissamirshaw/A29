#WAP generate nos 1 to 10 using recursion
def gene(n):
    if n==1:
        return 1
    else:
        return n, gene(n-1)
print(gene(1))
print(type(gene(1)))