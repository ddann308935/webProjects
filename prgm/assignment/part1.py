# Name: Daniel
# Date: 28/08/2024
# Purpose: Component 1 – creating a new user account (registration).
# This component takes a new username and password from the user and appends them to the existing file (accounts.txt). The user can choose their password with a mixture of characters, but the password must be checked to ensure it meets minimum length requirements. 

username = input("Please create a username: ")
password = input("Please create a password: ")

while len(password) < 8 :
    print("Password needs to be minimum 8 characters long.\nPlease create a password: ",end="")
    password = input("")

print()

account = open("/workspaces/Cert4IT/prgm/assignment/accounts.txt", "a")
account.write(f"{username},{password}\n")
account.close()

account = open("/workspaces/Cert4IT/prgm/assignment/accounts.txt", "r")
print(account.read())
account.close()
