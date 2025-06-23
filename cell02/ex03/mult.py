first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
mult = first_num * second_num
print(f"{first_num} x {second_num} = {mult}")
if mult > 0:
    print("The result is positive")
elif mult < 0:
    print("The result is negative")
else:
    print("The result is both positive and negative")

