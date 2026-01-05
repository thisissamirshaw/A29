#WAP to create a score card
while True:
 marks = int(input("Enter your marks :"))
 if 100 >= marks >= 90:
    print("first division")
 elif 89 >= marks >= 60:
    print("second division")
 elif  36 <= marks <= 59:
    print("third division")
 elif 0<= marks <= 35:
    print("fail")    
 else:
   print("Marks not in range")
 if marks == 999:
    print("end of programme")
    break
 