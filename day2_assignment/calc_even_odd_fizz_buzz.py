#calculator
num1 = int(input("Enter first number: "))
operand = input("Enter an operand (+, -, *, /): ")
num2 = int(input("Enter second number: "))

if operand == "+":
    answer = num1 + num2
    print(answer)
elif operand == "-":
    answer = num1 - num2
    print(answer)
elif operand == "*":
    answer = num1 * num2 
    print(answer)
elif operand == "/":
    answer = num1 / num2
    print(answer)
else: 
    print("Please enter a proper answer!")



#even odd
num = input("Enter a number: ")
if int(num) % 2 == 0:
    print("Even")
else:
    print("Odd")


# Fizz Buzz
number = input("Enter a number: ")
if int(number) % 3 == 0 and int(number) % 5 == 0:
    print("Fizz Buzz!")
elif int(number) % 3 == 0 and int(number) % 5 != 0:
    print("Fizz")
elif int(number) % 3 != 0 and int(number) % 5 == 0:
    print("Buzz")
else: 
    print("Try another number")
