#WAP to perform Anagram
a='silent'
b='silenl'
if len(a)==len(b):
    for i in a:
        if i not in b:
            print("not anagram")
            break
        else:
            pass
    print("anagram")
            