operator = input("What type of math question? (+ - * /): ")

num1 = float(input("What's the first number? "))
num2 = float(input("What's the second number? "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not valid, I can only calculate addition, subtraction, multiplication and fractions.")

input("Press enter to exit...")
