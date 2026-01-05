#WAP to check the character is vowel or consonent using nested if 
ch=input("enter character")
if ('a'<=ch<='z') or ('A'<=ch<='Z'):
    if ch in 'aeiouAEIOU':
        print("vowel")
    else:
        print("consonent")
else:
    print("not an alphabet")