import os

usernames = open("Users.txt").read().splitlines()

compareFile = open("CompareUsers.txt").read().splitlines()

userFound = False


# Compares the usernames and comparison usernames. If a username in Users.txt isnt in CompareUser.txt, it will add the user to the system
for i in usernames:
    for d in compareFile:
        if i == d:
            userFound = True
            continue
    if userFound == False:
        os.system("useradd " + i)
        print("User not found " + i)
    userFound = False

for i in compareFile:
    for d in usernames:
        if i == d:
            userFound = True
        
            continue
    if userFound == False:
        os.system("userdel " + i)
        print("User not found " + i)
    userFound = False

os.system("cp Users.txt CompareUsers.txt")