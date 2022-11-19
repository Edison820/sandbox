MIN_LENGTH = 6


def main():
    password = get_name()
    stars(password)


def stars(password):
    print('*' * len(password))


def get_name():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f"Invalid. Please enter at least {MIN_LENGTH} character")
        password = input("Enter password: ")
    return password


main()