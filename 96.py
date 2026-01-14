# #WAP to check login credentials for the operations.
user_name='xyz@123'
pass_word="1234"
while True:
    count=3
    user=input("Enter User Name: ")
    password=input("Enter password:")
    if user==user_name and password==pass_word:
        print("\n-----Welcome to programme-----")
        break
    else:
        print("Wrong credentials try again")