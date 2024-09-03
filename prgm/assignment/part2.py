# Name: Daniel
# Date: 31/08/2024
# Purpose: Component 2 – checking a username and password (logging in). Takes an existing username and password (for a previously registered user) and checks if they match a valid entry in the file (accounts.txt).

username = input("Please enter a username: ")
password = input("Please enter a password: ")

account = open("/workspaces/Cert4IT/prgm/assignment/accounts.txt", 'r')


