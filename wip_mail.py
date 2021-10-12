#python -m smtpd -c DebuggingServer -n localhost:1025

import os 
import smtplib, ssl
from email.message import EmailMessage

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "k4jo73@gmail.com"
receiver_email = "k4jo73@outlook.com"

msg = EmailMessage()
msg.set_content('This is my message')
msg['Subject'] = 'Subject'
msg['From'] = sender_email
msg['To'] = receiver_email

# password = input("Type your password and press enter: ")
password = os.environ.get('PythonGMailPwd')

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
    # server.sendmail(sender_email, receiver_email, msg,)
    server.send_message(msg)
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 