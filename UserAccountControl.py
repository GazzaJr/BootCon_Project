import os

# Get action from user
print("What action would you like to perform? \n1. Add Users\n2. Remove users\n3. Add users to group\n4. Remove users from group")
userAction = input("::")


loopCondition = True
# Get file location
while loopCondition:
    print("Where is the file located? (Absoulte path preferred)")
    fileLocation = input("::")
    if fileLocation.endswith("txt"):
        loopCondition = False

# Opens the file specified above and converts it into a list seperated by line.
usernames = open(fileLocation).read().splitlines()
print(usernames)

def addUser():
    for i in usernames:
        os.system("useradd " + i)
        print("Added User called " + i)


# Added in a requirement to verify that you want to delete all the users.
def removeUser():
    print("Reached here")
    loopCond = True
    while loopCond:
        verify = input("Are you sure you want to delete these users, this action is irreversible. Write yes or no\n::")
        if verify == "yes":
            loopCond = False
        elif verify == "no":
            return
        else:
            print("Please select an option\n")


    for i in usernames:
        os.system("userdel -r " + i)
        print("Removed User called " + i)

if userAction == "1":
    addUser()
elif userAction == "2":
    removeUser()