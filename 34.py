#WAP to print last character of a list and it should be string and palindrome in nature and its length should be more than 4 without using any inbuilt functions
lst=['hello','aba','121','world','python']
last=lst[ -1]
if isinstance(last, str) and len(last) > 4:
    # Check if palindrome manually
    is_palindrome = True
    for i in range(len(last)):
        if last[i] != last[len(last) - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print("Last character:", last[-1])
    else:
        print("Not a palindrome")
else:
    print("Condition not met")