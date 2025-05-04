import re

sentence = input("Enter a sentence: ")

if re.match(r'^ython', sentence, re.IGNORECASE):
    print("The sentence starts with 'python'.")
else:
    print("The sentence does not start with 'python'.")

if re.search(r'python', sentence, re.IGNORECASE):
    print("The sentence contains the word 'python'.")
else:
    print("The sentence does not contain the word 'python'.")

digits = re.findall(r'\d', sentence)
print("All digits in the sentence:", digits)

uppercase = re.findall(r'[A-Z]', sentence)
print("All uppercase characters in the sentence:", uppercase)

lowercase = re.findall(r'[a-z]', sentence)
print("All lowercase characters in the sentence:", lowercase)

alphanumeric = re.findall(r'[A-Za-z0-9]', sentence)
print("All alphanumeric characters in the sentence:", alphanumeric)


three_digit_numbers = re.findall(r'\b\d{3}\b', sentence)
print("All three-digit numbers:", three_digit_numbers)

vowels = re.findall(r'[aeiouAEIOU]', sentence)
print("All vowels in the sentence:", vowels)

consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', sentence)
print("All consonants in the sentence:", consonants)

special_symbols = re.findall(r'[^a-zA-Z0-9\s]', sentence)  # Anything that's not a letter, digit, or whitespace
print("All special symbols in the sentence:", special_symbols)

whitespaces = re.findall(r'\s', sentence)
print("All white spaces in the sentence:", whitespaces)

if re.search(r'\d', sentence):
    print("The sentence contains at least one digit.")
else:
    print("The sentence does not contain any digits.")


alphanumeric_count = len(re.findall(r'[A-Za-z0-9]', sentence))
if alphanumeric_count >= 2:
    print("The sentence contains at least two alphanumeric characters.")
else:
    print("The sentence does not contain at least two alphanumeric characters.")

digits = re.findall(r'\d', sentence)
if len(digits) <= 5:
    print("The sentence contains at most five digits:", digits)
else:
    print("The sentence contains more than five digits.")

characters = re.findall(r'\S', sentence)  # Find all non-whitespace characters
if len(characters) <= 5:
    print("The sentence contains at most five characters:", characters)
else:
    print("The sentence contains more than five characters.")

words_2_to_4 = re.findall(r'\b\w{2,4}\b', sentence)
print("All words with 2 to 4 characters:", words_2_to_4)

if re.search(r'python$', sentence, re.IGNORECASE):
    print("The sentence ends with 'python'.")
else:
    print("The sentence does not end with 'python'.")

result = re.findall(r'[^a\s]', sentence)  # Exclude 'a' and whitespace
print("All digits, alphabets, and special symbols except 'a':", result)
