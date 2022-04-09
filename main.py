from utils import view, add

while True:
    mode = input("Would you like to add a new password or view existing ones? (view/add). Press q to quit. ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode")
        continue


