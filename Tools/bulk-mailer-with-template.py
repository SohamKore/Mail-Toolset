import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configurations 
# Creaet multiple configs from multiple mails and use them if your mail quota is reached
sender_email = 'YOUR_MAIL_HERE@gmail.com'
sender_password = 'YOUR-APP-PASSWORD' # Enter pass that you got from creating app
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# List of recipients
recipients = [
    'Daddy.o@gmail.com',
    'olivia516@gmail.com',
    'avery822@gmail.com'
   
]
# Email content
subject = ' '
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Never gonna give you up, Never gonna let you down!, yes i just rick rolled</title>
</head>
<body>
    he he BAAALLLLSSSSSS!
</body>
</html>
'''

# Create the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject

# Attach the HTML content to the container
msg.attach(MIMEText(html_content, 'html'))

try:
    # Create an SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email to each recipient
        for recipient in recipients:
            msg['To'] = recipient
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")

    print("Bulk email sending completed.")
except smtplib.SMTPException as e:
    print("Error: Unable to send email.")
    print(str(e))
