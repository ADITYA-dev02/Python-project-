try:
    result = eval(input("Enter a variable name: ")) + 5
except NameError:
    result = "NameError: variable not defined"

print("Result:", result)
