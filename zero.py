a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))

try:
    result = a / b
except ZeroDivisionError:
    result = 'undefined'

print("Result:", result)
