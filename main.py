# Alexander Mullen, 10/25/2023


quit_option = False
option = ""
unencoded_password = ""
encoded_password = ""


def print_menu():
    global option
    global unencoded_password
    global encoded_password

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    option = input("Please enter an option: ")


def encode(password):
    l = ""
    for num in password:
        count = 3
        while count > 0:
            num = int(num)
            num += 1
            if num > 9:
                num = 0
            count -= 1
        l += str(num)
    return l


def main():
    global quit_option
    global unencoded_password
    global encoded_password

    while not quit_option:

        print_menu()
        if option == "1":
            unencoded_password = input("Please enter your password to encode: ")
            encoded_password = encode(unencoded_password)
            print("Your password has been encoded and stored!")

        if option == "3":
            quit_option = True


if __name__ == "__main__":
    main()