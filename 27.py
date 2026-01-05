#WAP to check the char is upper case , lower case ,number ,special char.

char = input("Enter a character: ")
if 'A'<= char <= 'Z':
    print(char,"is in upper case")
elif 'a' <= char <= 'z':
    print(char,"is in lower case")
elif '0'<= char <'9':
    print(char,"is a number")
else:
        print(char,"is special character")