x = int(input("enter the integer number: "))

while x > 9:
    digits = [int(digit) for digit in str(x)]
    product = 1
    for digit in digits:
        product *= digit
    x = product

print(x)