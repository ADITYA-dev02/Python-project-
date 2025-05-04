
user_dict = {'a': 1, 'b': 2}

key = input("Enter a key to access in the dictionary: ")


result = user_dict.get(key, "KeyError: key not found")

print("Result:", result)
