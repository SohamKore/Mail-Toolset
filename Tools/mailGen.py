import random

# List of common names
names = [
    # Write Names Directly!
    "robb", "JonSnow", "Jaime", "Ned", "Sean", "Rick", "Morty", "Jerry", "Birdperson", "Soham"
 ]




# Generate a list of 100 email addresses
email_list = [f"{name}{random.randint(1, 999)}@gmail.com" for name in random.choices(names, k=200)] # k = NUMBER_OF_MAILS TO GENERATE

# Print the email addresses
for email in email_list:
    print(email)
