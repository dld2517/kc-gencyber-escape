# import replit
# replit.clear()
import os
import pygame

loop=True
os.system('clear')


pygame.init()
x=400
y=400
scrn = pygame.display.set_mode((x,y))
pygame.display.set_caption('image')
imp = pygame.image.load("./blog.png").convert()
scrn.blit(imp, (0, 0))
pygame.display.flip()
status = True

def briefcase():
  os.system('clear') 
  i = 0
  while (i < 3):
      print('What is the combination (6 digits)?')
      combination = input('(To escape script, type "e")\n')
      if (combination == "e"):
            return;
      if (combination == "013088"):
            print("Correct! Take card #7\n")
            return;
      elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
      elif (i == 1): # Second incorrect guess
            print("Incorrect, try birthday MMDDYY.\n")
            i = i+1
      else: # Three strikes you're out!
            print("Incorrect. Take card #15\n")
            i = i+1
def laptop():
    os.system('clear')
    i = 0
    while (i < 3):
        print('What is the password?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "password"):
            print("Correct! Take card #8\n")
            return;
        elif (i == 0): # First incorrect guess
            print("Incorrect, try a very obvious and insecure password.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try again (lowercase).\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #29\n")
            i = i+1
def oranges():
    os.system('clear')
    i = 0
    while (i < 3):
        print('When will Suzanne attack? (Month day)')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "June 7" or combination == "June 07"):
            print("Correct! Take card #6\n")
            return;
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, be sure to read the codebook carefully.\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #2\n")
            i = i+1
def phone():
    os.system('clear')
    i = 0
    while (i < 3):
        print('What is the password?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "enigmamachine"):
            print("Correct! Take card #14\n")
            return;
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try again (lowercase and no space).\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #30\n")
            i = i+1
def target():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Who will Suzanne attack? (FIRST LAST)\n')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "ZOE WALKER"):
            print("Correct! Take card #23\n")
            return;
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try first and last name with space and all caps.\n")
            i = i+1
        else: # Three strikes you're out!
            print("Incorrect. Take card #5\n")
            i = i+1
def train():
    os.system('clear')
    i = 0
    while (i < 3):
        print('Where will Suzanne attack? (PLACENAME)\n')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "DISNEYLANDANAHEIM"):
            message="Correct! "
            card=3
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, try all caps with no space between words.\n")
            i = i+1
        else: # Three strikes you're out!
            message="Inorrect! "
            card=26
            menu(message,card)
            i = i+1
def wallet():
    os.system('clear')
    i = 0
    while (i < 3):
        print('What is the combination (NNN)?')
        combination = input('(To escape script, type "e")\n')
        if (combination == "e"):
            return;
        if (combination == "798"):
            message="Correct! "
            card=9
            menu(message,card)
        elif (i == 0): # First incorrect guess
            print("Incorrect, try again.\n")
            i = i+1
        elif (i == 1): # Second incorrect guess
            print("Incorrect, look carefully at the watch.\n")
            i = i+1
        else: # Three strikes you're out!
            message="Inorrect! "
            card=33
            menu(message,card)
            i = i+1

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
      loop=False
      return loop
    else:
      print ('Wrong')

while loop:
  print ('\n\n\nWill you escape?\n\n')
  message="Use your crypto seneses!"
  card=0
  loop=menu(message,card)

pygame.quit()
print("Thanks for playing!")
