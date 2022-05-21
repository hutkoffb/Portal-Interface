# Contains information for the charactor's attributes and belongings

# Dictionary Statments
classList = ['Fighter', 'Wizard', 'Rogue', 'Cleric']
classesLevel = {'Fighter': 0, 'Wizard': 0, 'Rogue': 0, 'Cleric': 0}
attributes = {'class': 'none', 'health': 0, 'strength': 0, 'intelligence':0, 'wisdom': 0, 'dexterity': 0, 'constitution': 0, 'charisma': 0}

################################################################################################
# Function: charCreation
# Description: 
# Parameters: n/a
# Return Values: 
################################################################################################
def charCreation():
    print("Which class would you like to start as?\n")
    
    print("1. Fighter | 2. Wizard | 3. Rogue | 4. Cleric ")

    while True:
        try:
            classChoice = str(input("Enter an option: "))
            if(classChoice == 'quit' or (int(classChoice) >= 1 and int(classChoice) <= 4)):
                break
            if(classChoice < 1 or classChoice > 4):
                quit()
        except: 
            print("Invalid choice. Enter an option 1 through 4.\nIf you wish to exit to the title screen, type quit.")

    

################################################################################################
# Function: charCreation
# Description: 
# Parameters: n/a
# Return Values: 
################################################################################################
attributes['health'] = some_value

def main():
    charCreation()

main()

