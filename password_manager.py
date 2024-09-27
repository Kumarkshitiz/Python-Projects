from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

key = load_key() 
fer = Fernet(key)

def view():
    with open ("password.txt", 'r')as f:
        for line in f.readlines():
            user , passw  =   line.rstrip().split("|")
            print(f"User:  {user}  |  Password:  {fer.decrypt(passw.encode()).decode()}")

def add():
    name = input("Account name : ")
    pwd = input("Password: ")
    with open("password.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add a new password or view an existing one ? (view / add )or  quit the program  q  ").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add() 
    else :
        print("Invalid mode !!")

print("Good Bye !")