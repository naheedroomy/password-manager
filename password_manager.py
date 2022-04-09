
def view():
    pass


def add():
    name = input("Account name: ")
    master_pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        pass


pwd = input("what is the master password?")


while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add). Press q to quit").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue


