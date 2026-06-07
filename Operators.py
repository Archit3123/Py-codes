# Calculator program that performs basic arithmetic operations based on user input.
print('Give the first operand and the second operand')
a = int(input('First operand: '))
b = int(input('Second operand: '))
print("Operation choices: +, -, *, /")
operation = input("Choose an operation: ")
if operation == '+':
    result = a + b  
elif operation == '-':
    result = a - b 
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed."
print("Result:", result)