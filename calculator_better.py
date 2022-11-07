num1 = float(input("Enter the first number: "))
op = input(" enter any of +,-,/,*, Enter operation: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator, enter any of +,-,/,*")