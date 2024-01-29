master_pwd = input("What is the master password? ")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "| Password:", password)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (add, view)? Press 'q' to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        pass
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")