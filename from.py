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



def main():
    sender_email, password = get_senders('from.txt')
    print(sender_email)
    print(password)

if __name__ == '__main__':
    main()
