import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configurations
sender_email = 'YOUR_MAIL_HERE@gmail.com'
sender_password = 'YOUR-APP-PASSWORD' # Enter pass that you got from creating app
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# List of recipients
recipients = [
    'Jaimebethblog@gmail.com',
    'justforyou091994@gmail.com'
]

# Email content
subject = '🔥💪 Doofenshmirtz Evil Incorporated!'

# ADD YOUR OWN HTML HERE
html_content = '''

<!DOCTYPE html>
<html>
<head>
    <style>
        /* General Styles */
    *{
        balls:mega-size;
        brain: big-brain;
        pp: mega-pp;
        pew: die-pie;
    }
    </style>
</head>

<body>

    <script>
        function scrollOrder() {
            const section = document.querySelector(".orderBtn");
            section.scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>
</html>
'''

# Create the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['Subject'] = subject

# Attach the HTML content to the container
msg.attach(MIMEText(html_content, 'html'))

# File paths for successful and failed emails to store in
# Enter exact path if it doesent work
successful_emails_file = r'successful_emails.txt'
failed_emails_file = r'failed_emails.txt'

try:
    # Create an SMTP session
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email to each recipient
        successful_emails = []
        failed_emails = []
        for recipient in recipients:
            msg['To'] = recipient
            response = server.sendmail(sender_email, recipient, msg.as_string())
            if len(response) == 0:
                print(f"Email sent to {recipient}")
                successful_emails.append(recipient)
            else:
                print(f"Failed to send email to {recipient}")
                failed_emails.append(recipient)

    print("Bulk email sending completed.")

    # Append successful emails to a text file
    with open(successful_emails_file, 'a') as file:
        for email in successful_emails:
            file.write(email + '\n')

    # Append failed emails to a text file
    with open(failed_emails_file, 'a') as file:
        for email in failed_emails:
            file.write(email + '\n')

    print("Successfully sent emails added to the file.")

except smtplib.SMTPException as e:
    print("Error: Unable to send email.")
    print(str(e))
