import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender = '24012011142@gun.ac.com'
receiver = 'vatsalpatel0609@gmail.com'

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = 'Sending Image From Python'

body = "Hello, this is a test email with an image attachment sent from Python."
msg.attach(MIMEText(body, 'plain'))

file = open('Python.png' , 'rb')
attachment = MIMEApplication(file.read(), name='Python.png')
attachment['Content-Disposition'] = 'attachment; filename="Python.png"'
msg.attach(attachment)

# 4. Connect to SMTP server and send the email
smtpob = smtplib.SMTP('smtp.gmail.com', 587)
smtpob.starttls()
# Use your 16-character App Password here
smtpob.login(sender, "your_16_character_password") 

smtpob.sendmail(sender, receiver, msg.as_string())
smtpob.quit()

print("Email sent successfully!")
