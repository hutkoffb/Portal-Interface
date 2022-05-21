# Term Project, User Login
# Author: Benjamin Hutkoff
# Date: May 18th, 2022

import random as rand
import csv
import time

################################################################################################
# Function: login_info
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def login_info():
    # Using csv reader
    rows = []
    with open("userInfo.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #print(header)
    print(rows)

    return rows

################################################################################################
# Function: username_input
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def username_input():   
    while True:
        try:
            # user enters username
            username = str(input("Enter Username: ")) 
            return username
        except:
            print("ERROR: Username is not of type string.")

################################################################################################
# Function: username_check
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def username_check(user_info, username):
    count1 = 0 
    count2 = 0
    # checks each username index and compares it to the input username
    for x in range(len(user_info)):
        if(username == user_info[count1][count2]):
            print("Valid Username")
            return count1
        count1 += 1

################################################################################################
# Function: password_input
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def password_input():
    while True:
        try:
            # user enters username
            password = str(input("Enter Password: ")) 
            return password
        except:
            print("ERROR: Password is not of type string.")

################################################################################################
# Function: password_check
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def password_check(user_info, password, count1): 
    count2 = 1
    
    # checks each username index and compares it to the input username
    if(password == user_info[count1][count2]):
        print("Logging in...\n")
        time.sleep(2)
        return True
    else:
        print("Password and Username do NOT match.")
        return False


################################################################################################
# Function: homepage
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def homepage(username):
    print(f"Welcome, {username}!\n")

    print("Here are a list of available options:")
    


################################################################################################
# Function: main
# Description: 
# Parameters: n/a
# Return Values: 
# Pre-Conditions: n/a
# Post-Conditions: n/a
################################################################################################
def main():
    user_info = login_info()
    match = False

    while match == False:
        # Username input for user
        username = username_input()
        # Checks to see that username exists
        count1 = username_check(user_info, username)
        # Password input for user
        password = password_input()
        # Checks to see if username and password match
        match = password_check(user_info, password, count1)
    homepage(username)

# Driver Code for the file
main()