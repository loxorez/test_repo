import smtplib, ssl
import os

EMAIL_PASS = os.environ.get('MY_EMAIL_PASSWORD')
SENDER = 'y89@ukr.net'
RECEIVER = 'vkondratiuk@larch-networks.com'
SUBJECT = 'Learning smtplib'
BODY = 'I did it!'

message_template = f"""From: Vitalii Kondratiuk <{SENDER}>
To: <{RECEIVER}>
Subject: {SUBJECT}

{BODY}
"""

ssl_secure_connection = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.ukr.net", 465, context=ssl_secure_connection) as smtp:
    smtp.login(SENDER, EMAIL_PASS)
    smtp.sendmail(SENDER, RECEIVER, message_template)

