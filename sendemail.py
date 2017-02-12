import smtplib

from_name = 'Samath Scott'
from_addr = 'myemail@gmail.com'
to_name  = 'Evanna Clarke'
to_addr = 'evvClarke@yahoo.com'
subject = 'Very Important'
msg = "This is a reminder of our meeting"

message = """From: {} <{}> To: {} <{}> Subject: {} {} """ 

message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)

# Credentials (if needed)
username = 'myemail@gmail.com'
password = ''

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit()
