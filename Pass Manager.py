from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
   file = open("key.key", "rb")
   key = file.read()
   return key



key = load_key()
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("/")
            print("user:", user, "Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Acc Name ")
    pwd = input("Password ")

    with open("passwords.txt", "a") as f:
        f.write(name + "/" + fer.encrypt(pwd.encode()).decode() + "\n" )


while True:

    mode = input("New or View? ")
    if mode == "View".lower():
        view()
    elif mode == "New".lower():
        add()
    else:
        print("No mode")
    continue
