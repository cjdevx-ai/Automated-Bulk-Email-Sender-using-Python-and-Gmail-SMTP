import smtplib
import ssl
import time
import pandas as pd
from email.message import EmailMessage

# Define email sender
email_sender = 'sample@gmail.com'
email_password = 'xxxx xxxx xxxx xxxx' #read Readme.md for the tutorial to get your own password

# Load CSV
df = pd.read_csv("emails.csv")   # must have column: email_add
email_receivers = df['email_add'].dropna().tolist()

# Set the subject and body of the email
subject = 'this is your SUBJECT' 

#edit email body
body = """
this is your BODY 
"""

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in once and send emails in a loop
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    print("Sending emails to:", email_receivers)

    for receiver in email_receivers:
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        smtp.sendmail(email_sender, receiver, em.as_string())
        print(f"Email sent to {receiver}")
        time.sleep(2)
