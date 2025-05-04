
user_list = [10, 20, 30]

# Get user input for the index
index = int(input("Enter an index to access in the list: "))

# Try to access the list and handle IndexError
try:
    result = user_list[index]
except IndexError:
    result = "IndexError: index out of range"

print("Result:", result)
