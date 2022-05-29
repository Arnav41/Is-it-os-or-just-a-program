import time
import os

print("""

███████████████████████████████████████████████████
██▀▄─██▄─▄▄▀█▄─▀█▄─▄██▀▄─██▄─█─▄█▀▀▀▀▀██─▄▄─█─▄▄▄▄█
██─▀─███─▄─▄██─█▄▀─███─▀─███▄▀▄█████████─██─█▄▄▄▄─█
▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▀▄▄▀▀▀▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▀▄▄▄▄▄▀
""")


print("""
Wait a few seconds for the setup wizard to run ::---->
""")
time.sleep(1)
print("""
[1]. start setup
[2]. already a user
[3]. quit
""")

def Credentialsdata():
    with open('Credentials/creds-name.txt', 'w') as f:
        f.writelines(name)
    with open('Credentials/creds-pass.txt', 'w')as f:
        f.writelines(passw)
#setup for username&pass
setup_input = input("[?]: ")
if setup_input == "1":
    name = input("enter your name: ")
    passw = input("enter a password: ")
    Credentialsdata()

    print("start the program again!, and select 'already a user' ")
    print("closing this session in 5sec")
    time.sleep(6)


#already a user->
if setup_input == "2":
    login_username = open('Credentials/creds-name.txt')
    login_pass = open('Credentials/creds-pass.txt')
    lp = login_pass.read()
    lu = login_username.read()
    
while True:
        loginput = input("enter your password " + lu + ": ")
        if loginput == lp:
            os.startfile("home.py")
            os.abort
        else:
            print("wrong")
            break


if setup_input == "3":
    os.abort
time.sleep(284)


