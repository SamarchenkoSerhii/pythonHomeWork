digit1  = int(input("Please enter a first  number: "))
digit2  = int(input("Please enter a second number: "))
operation  = input("Please select operation +, -, / or *  :")
if operation == "+" :
    print(digit1,operation,digit2, "=",digit1 + digit2)
elif operation == "-" :
    print(digit1,operation,digit2, "=",digit1 - digit2)
elif operation == "*":
    print(digit1,operation,digit2, "=",digit1 * digit2)
elif operation == "/" and digit2 != 0:
    print(digit1,operation,digit2, "=",digit1 / digit2)
else:
    print("incorrect input data")
    if operation == "/" and digit2 == 0:
        print("the divisor cannot be zero")

