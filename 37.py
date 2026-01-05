# WAP Take age as input.If age is valid (> 0), then:if age < 13 → "Child" else if age <= 19 → "Teen" else → "Adult" Else → "Invalid age
age = int(input("Enter age"))
if age >= 0 :
    if 0 < age <= 12:
        print("child")
    else:
        if 13 <= age <= 19 :
            print("Teen")
        else:
            print("Adult")
else:
    print("Invalid age")   