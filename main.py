import os

loop=1
os.system('clear')


def briefcase():
  os.system('clear') 
  i = 0
  while (i < 3):
      print('Briefcase\nWhat is the combination (6 digits)?')
      combination = input('(To escape script, type "e")\n')
      if (combination == "e"):
            return 0
      if (combination == "013088"):
            message="Correct! One step closer!\n"
            card=7
            menu(message,card)
      elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
      elif (i == 1): # Second incorrect guess
            print("Incorrect, try birthday MMDDYY.\n")
            i = i+1
      else: # Three strikes you're out!
            print("Incorrect. Take card #15\n")
            i = i+1
            return 0
  

def laptop():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Laptop\nWhat is the password?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "password"):
            message="Correct! One step closer!\n"
            card=8
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try a very obvious and insecure password.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try again (lowercase).\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #29\n")
            i = i+1
            return 0
            
def oranges():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Oranges\nWhen will Suzanne attack? (Month day)')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "June 7" or combination == "June 07"):
            message="Correct! One step closer!\n"
            card=6
            menu(card,message)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, be sure to read the codebook carefully.\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #2\n")
            i = i+1
            return 0
            
def phone():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Phone\nWhat is the password?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "enigmamachine"):
            message="Correct! One step closer!\n"
            card=14
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try again (lowercase and no space).\n")
            i = i+1
        else: # Three strikes you're out!
            message="Incorrect. Take card #30\n"
            i = i+1
            return 0
            
def target():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Target\nWho will Suzanne attack? (FIRST LAST)\n')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "ZOE WALKER"):
            message="Correct! Almost there!\n"
            card=23
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try first and last name with space and all caps.\n")
            i = i+1
        else: # Three strikes you're out!
            message="Incorrect. Take card #5\n"
            i = i+1
            return 0
            
def train():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Train\nWhere will Suzanne attack? (PLACENAME)\n')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "DISNEYLANDANAHEIM"):
            message="Correct! You have SAVED THE DAY!"
            card=3
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try all caps with no space between words.\n")
            i = i+1
        else: # Three strikes you're out!
            message="Incorrect! Take card #26\n"
            i=i+1
            return 0
            
def wallet():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Wallet\nWhat is the combination (NNN)?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return 0
        if (combination == "798"):
            message='Correct! '
            card=9
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print('Incorrect, try again.\n')
            i = i+1
        elif (i == 1): # Second incorrect guess
            print('Incorrect, look carefully at the watch.\n')
            i = i+1
        else: # Three strikes you're out!
            message='Incorrect! Take card #6\n'
            i=i+1
            return 0
            
def menu(message,card):
    print ('\n\n\nWill you escape?\n\n')
    print (message,'See card',card,'for instructions!')
    print (20*'-','\n\n\n')
    print ('1. Briefcase')
    print ('2. Laptop')
    print ('3. Oranges')
    print ('4. Phone')
    print ('5. Target')
    print ('6. Train')
    print ('7. Wallet')
    print ('8. Quit')
    choice=input('Enter your choice number: ')
    if (choice == '1'):
      briefcase()
    elif (choice == '2'):
      laptop()
    elif (choice == '3'):
      oranges()
    elif (choice == '4'):
      phone()
    elif (choice == '5'):
      target()
    elif (choice == '6'):
      train()
    elif (choice == '7'):
      wallet()
    elif (choice == '8'):
      return 0
    else:
      print ('Wrong')

while loop:
  print ('\n\n\nWill you escape?\n\n')
  message='Use your crypto seneses!'
  card=0
  loop=menu(message,card)

print('Thanks for playing!')