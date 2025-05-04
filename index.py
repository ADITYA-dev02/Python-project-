user_list = [10, 20, 30]
index = int(input("Enter an index to access in the list: "))
try:
    result = user_list[index]
except IndexError:
    result = "IndexError: index out of range"
print("Result:", result)
