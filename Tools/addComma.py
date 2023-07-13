
def format_email_list(email_list):
    formatted_list = [f"    '{email.strip()}' " for email in email_list if email.strip()]
    return formatted_list

# Example usage
input_emails = '''
drshikhasingh24@gmail.com 
Fatgirlfedup1@gmail.com 
nehadietclub@gmail.com 
weightlossmealsofficial@gmail.com 
eatmorelosemore7@gmail.com 
gunjanmehta2296@gmail.com 
office@kularbariatrics.com 
drkskular@gmail.com 
justforyou091994@gmail.com 
tanvi.069@gmail.com 
'''

emails_list = input_emails.split('\n')
formatted_emails = format_email_list(emails_list)
for email in formatted_emails:
    print(email)
