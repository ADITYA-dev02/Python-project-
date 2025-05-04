import re

email = input("Enter an email address to validate: ")

email_regex = r'^\w+@[a-zA-Z]+\.com'

if re.match(email_regex, email):
    print("Valid email:", email)
else:
    print("Invalid email:", email)

phone_number = input("Enter a phone number to validate: ")

phone_regex = r'^\d{3}[-\s.]?\d{3}[-\s.]?\d{4}$'

if re.match(phone_regex, phone_number):
    print("Valid phone number:", phone_number)
else:
    print("Invalid phone number:", phone_number)
