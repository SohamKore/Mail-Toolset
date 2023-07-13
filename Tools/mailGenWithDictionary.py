import random
import json

# Read names from file
with open('name-dictionary.txt', 'r') as file:
    names = file.read().split(',')

# Strip whitespace from names
names = [name.strip() for name in names]

# Generate a list of 100 email addresses
email_list = [f"{name}{random.randint(1, 999)}@gmail.com" for name in random.choices(names, k=200)]

# Print the email addresses
for email in email_list:
    print(email)

# Convert names to JSON format
names_json = json.dumps(names)

# Write names to a JSON file
with open('names.json', 'w') as file:
    file.write(names_json)
