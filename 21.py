#WAP to check the character is special character
a=input("enter any character")
if not(('a'<=a<='z') or ('A' <=a<='Z') or ('0'<= a<='9')):
    print(True)
else:
    print(False)

    #if char in '~!@#$%^&*()_+=':