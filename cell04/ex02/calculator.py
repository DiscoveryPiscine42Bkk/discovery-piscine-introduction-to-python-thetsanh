num1 = int(input("Give me the first numbere: "))
num2 = int(input("Give me the second numbere: "))
print("Thank you!")
for i in ['+', '-', '/', '*']:
    if i == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif i == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif i == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {int(num1 / num2)}")
        else:
            print("Division by zero is not allowed.")
    elif i == '*':
        print(f"{num1} * {num2} = {num1 * num2}")