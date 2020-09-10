num = int(input("Enter a number: "))

def factorial():
    sol = 1
    for i in range(1, num + 1):
        sol *= i
    return sol
print(factorial())