First_number = float(input("Please enter first number "))
Operator = input("Please choose an operation +, -, / or * ")
Second_number = float(input("Please enter second number "))

if Operator == '+':
    result = First_number + Second_number
elif Operator == '-':
    result = First_number - Second_number
elif Operator == '/':
    result = First_number / Second_number
elif Operator == '*':
    result = First_number * Second_number
else:
    print("Please enter proper format")
print(result)

