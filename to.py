def get_targets(filename):
    #global target_email
    target_email = []

    with open(filename, mode='r', encoding='utf-8') as target_file:
        for line in target_file:
            target_email.append(line.split()[0])

    return target_email



def main():
    target_email = get_targets('to.txt')
    print(target_email)


if __name__ == '__main__':
    main()
