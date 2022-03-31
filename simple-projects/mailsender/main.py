from email import message
from http import server
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email From Python"
body = "This is a test email form Python!"
sender_email = "userwpstec01@gmail.com"
receiver_email = "userwpstec01@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
#message["From"] = sender_email
message["From"] = "John Doe"
message["To"] = receiver_email
message["Subject"] = subject
# message.set_content(body) # to use plaintext uncomment this

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")  # to use html uncomment this

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")
