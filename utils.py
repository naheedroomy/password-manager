from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('passwords.txt', "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pwd = data.split("|")
            print({
                "user": user,
                "password": fer.decrypt(pwd.encode()).decode()
            }
            )


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


key = load_key()
fer = Fernet(key)
