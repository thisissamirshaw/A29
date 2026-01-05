#WAP to store username and password and validte it using nested if .
username=input("enter username")
password=input("enter password")
if username=="admin":
    if password=="12345":
        print("login successful")
    else:
        print("invalid password")
else:
    print("invalid username")