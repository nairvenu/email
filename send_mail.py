import smtplib
from time import gmtime, strftime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#remove 2FA and allow less secure apps
sender_email = 'nairvenu.tata@gmail.com'
sender_email1 = 'venunair149@gmail.com'
password = 'Bulwark#321'
password1 = 'Venunair123'

target_email = 'siddharth.gupta@bulwarkx.com'

file=open('body.txt', 'r')   #define email body
body=file.read()

#print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(sender_email, password)




msg = MIMEMultipart()       # create a message


# setup the parameters of the message
msg['From']=sender_email
msg['To']=target_email
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(body, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)
s.quit()

print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))


s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()

s.login(sender_email1, password1)
msg = MIMEMultipart()       # create a message


# setup the parameters of the message
msg['From']=sender_email1
msg['To']=target_email
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(body, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
