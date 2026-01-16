#WAP to extract all the uppercase alphabet from a given string
a=input("enter a string")
for i in a:
    if 'a'<=i<='z':
        continue
    else:
        print(i)