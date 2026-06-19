# Create a basic calculator program that takes two numbers and an operator (+, -, *, /) as input, performs the correct operation using typecasting, and prints the result. If the user enters an invalid operator, print an error message.


number1 = int(input("enter number")) 
number2 = int(input("enter number"))
operator = input("enter operator")

match operator:
    case "+":
        print(number1+number2)
    case "-":
        print(number1-number2)
    case "*":
        print(number1*number2)
    case "/":
        print(number1/number2)
    case _: 
        print("invalid operator")