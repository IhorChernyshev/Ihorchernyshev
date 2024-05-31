first_number = int(input('write first number'))
second_number = int(input('write second number'))
third_operation = input("write operation")
if third_operation == '+':
    print(first_number + second_number)
elif third_operation == '-':
    print(first_number - second_number)
elif third_operation == '/' and second_number != 0:
    print(first_number / second_number)
elif third_operation == '*':
    print(first_number * second_number)
else:
    print('Dividing by zero is not allowed')