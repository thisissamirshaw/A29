# #WAP to extract all the uppercase from given string using function.
# def extract_uppercase(s):
#     uppercase_chars = [char for char in s if char.isupper()]
#     return ''.join(uppercase_chars)
# input_string = input("Enter a string: ")
# result = extract_uppercase(input_string)
# if result:
#     print("Uppercase characters in the string are:", result)
# else:
#     print("No uppercase characters found in the string.")

def upper_c():
    a='PytHON'
    out=''
    for i in a:
        if 'A'<=i<='Z':
            out+=i
    print(out)
upper_c()      