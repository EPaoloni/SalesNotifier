import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail(htmlMessage, receiverAddress):
    if(htmlMessage == ""):
        return "Empty message"
    if(receiverAddress == ""):
        return "Empty Address"
    with open('resources/config/config.json') as json_file:
        data = json.load(json_file)
        sender_email = data['account-gmail']
        password = data['password-gmail']

    message = MIMEMultipart("alternative")
    message["Subject"] = "New games and Sales at Nintendo Argentina"
    message["From"] = sender_email
    message["To"] = receiverAddress

    part1 = MIMEText(htmlMessage, "html")

    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiverAddress, message.as_string()
        )
