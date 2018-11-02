import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_senders(filename):
    #global sender_email
    sender_email = []
    #global password
    password = []
    with open(filename, mode='r', encoding='utf-8') as sender_file:
        for line in sender_file:
            sender_email.append(line.split()[0])
            password.append(line.split()[1])
    return sender_email, password

def get_targets(filename):
    #global target_email
    target_email = []

    with open(filename, mode='r', encoding='utf-8') as target_file:
        for line in target_file:
            target_email.append(line.split()[0])

    return target_email



def main():

    sender_email, password = get_senders('from.txt')

    target_email = get_targets('to.txt')




# set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()

#loginloop
    for email,passwd in zip(sender_email, password):
        print ("loging in",email)

        s.login(email, passwd)



if __name__ == '__main__':
    main()
