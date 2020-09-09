def greet(name, age):
    print(f"Hello my name is {name} and I am {age} years old.")

greet("Dom", 26)

#name = input("Enter your name: ")
#print(name)


#num1 = input("enter first number: ")
#num2 = input("enter second number: ")

#result = int(num1) + int(num2)
#print(result)


#dollar1 = input("Enter first dollar amount: ")
#dollar2 = input("Enter second dollar amount: ")

#total = float(dollar1) + float(dollar2)
#print(total)


def calculate_tip(total, percentage):
    return total * (percentage/100)

tip = calculate_tip(100, 30)
if tip >= 15:
    print("Wow you're amazing!")
elif tip >= 5 and tip <= 10:
    print("Thank you")
else:
    print("You need to learn some manners")
print(tip)

