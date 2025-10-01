a = int(input('Enter first number\n'))
b = int(input('Enter second number\n'))
operation = input('Enter operation')

if operation == 'add':
    result = a + b
    print(f"Result of addition is {result}")
elif operation == "subtract":
    result = a - b
    print(f'Result of subtraction is {result}')
else:
    print("There is no such operation")
