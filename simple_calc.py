method = input("What method do you what to use, +, -, *, /: ")
while (method not in ["+", "-", "*", "/"]):
    print("WHAT THE HECK ARE YOU TYPING!?")

    method = input("What method do you what to use, +, -, *, /: ")

number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))

if method == "+":
    print(number1 + number2)
    
elif method == "-":
    print (number1 - number2)
    
elif method == "*":
    print (number1 * number2)
    
elif method == "/":
    print (number1 / number2)   
