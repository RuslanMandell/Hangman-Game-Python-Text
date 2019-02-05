#Ruslan Mandell
#Hangman Game
#10/5/2018
#goal of the game is to guess the hidden word,
#either by guessing it letter by letter or by
#typing the full word.



import random

#--- List of topics with words based off of the topic in each one ---#

listFiles = ["SeaCreatures.txt","Fruits.txt","Countries.txt"]

#--- Chooses random topic from list and extracts a random word,
#--- from that topic ---#

chosenTopic = listFiles[random.randint(0,len(listFiles)-1)]

file = open(chosenTopic,'r')


#--- Splits each word by \n which moves it down ---#
listOW = []
listOW = file.read().split("\n")

file.close()


#--- Choses the random word from the list of words ---#
randomL = random.choice(listOW)


#--- Length of the random chosen word ---#
wLen = len(randomL)

#--- List of used letters ---#
LOUL = []

#--- List of unmasked letters ---#
uLetters = []

#--- List of the letters in the chosen word ---#
listW = list(randomL)
#--- List of the letters in the chosen word but uppercase --#
listWU = list(randomL.upper())

turns = 8

iS =  True
sMenu = True
game = False
rules = False
low = False







for i in range (wLen):
    uLetters.append("_")

print("\t\t\t _\n"
     "\t\t\t| |\n"
     "\t\t\t| |\n"
     "\t\t\t| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __ \n"
     "\t\t\t| |_ \ / _` | |_ \ / _` | |_ ` _ \ / _` | |_ \ \n"
     "\t\t\t| | | | (_| | | | | (_| | | | | | | (_| | | | |\n"
     "\t\t\t|_| |_|\____|_| |_|\___ |_| |_| |_|\____|_| |_|\n"
     "\t\t\t                    __/ |                      \n"
     "\t\t\t                   |___/                       \n")


print("1.start","\n2.rules","\n3.list of words (for the topic)","\nTopic:",chosenTopic.replace(".txt",""))


while iS == True:
    #--- Start Menu ---#

    #--- When the user runs the prgram it autmoatically displays a list ---#
    #--- of options the user could choose from before starting the game ---#
    #--- such as (rules, the game and the list of words ) ---#

    if sMenu == True:
        sChoose = input("What would you like to do? (1,2,3) ")

        if sChoose == '1':
            sMenu = False
            game = True
            break


        elif sChoose == '2':
            sMenu = False
            rules = True

        elif sChoose == '3':
            sMenu = False
            low = True
        else:
            print("Invalid Command")


    #####################

    #--- List Of Provided Words ---#


    #--- Determines whether the user chose to view the list of ---#
    #--- words that could be chosen until the user choses otherwise ---#

    if low == True:
            print("\n","\n• ".join(listOW))

            print("\n1.start", "\n2.rules")
            sChoose = input("\nWhat would you like to do? (1,2) ")
            if sChoose == '1':
                low = False
                game = True
                break

            if sChoose == '2':
                low = False
                rules = True
            else:
                print("Invalid Command")


    #################################


    #--- Rules Of The Game ---#

    #--- Determines whether the user chose to view the rules and if so displays them ---#
    #--- until the user choses otherwise ---#

    if rules == True:
        #instructs the user what the game is about and what to do
        print("\n\t\t\t\t\t\tWelcome To Hangman\n \tThe goal of the game is to guess the word that is hidden, either \n",
              "\t\t by guessing the letters singularly or the whole word.",
              "\n\t\tA guess that is longer than one letter other than the whole",
              "\n\tword itself, or a number is invalid and will not count as a turn",
              "\n\t\t\t\t\tyou have 8 turns, don't mess up ;)")

        print("\n1.start", "\n2.list of words")
        sChoose = input("\nWhat would you like to do? (1,2) ")
        if sChoose == '1':
            rules = False
            game = True
            break


        if sChoose == '2':
            rules = False
            low = True
        else:
            print("Invalid Command")



    ##########################



#--- Game ---#

#--- this code runs when the user decides to start the game ---#
#--- at the beggining or after viewing the rules and the ---#
#--- list of words ---#

while game == True:


    #--- for loop set to 8 determining the max amount of turns ---#
    #--- the user has in this case it is eight ---#
    for i in range(8):

        #--- At the beggining of the game telling the user the topic and how long the word is ---#
        print("\nthe random topic is",chosenTopic.replace(".txt",""), "and your word is", " ".join(uLetters), "letters long")
        guess = input("\nguess the word/letters ")

        #--- Determines whether the users guess is one letter long then puts it into a list ---#
        if len(guess) == 1 and guess.isalpha() and guess not in LOUL:

            LOUL.append(guess.lower())

        #--- Determines whether the users guess is longer than 2 letters long and if is not equal|
        #--- to the whole word ---#
        if len(guess) >= 2 and guess != randomL and guess != randomL.upper() or guess.isdigit():
            print("Invalid, guess can only be one letter or the full word")

        #--- Determines whether the users guess is incorrect and removes a turn ---#
        if guess not in listW and len(guess) == 1 and guess.isalpha():
            turns -=1
            print("you're wrong you have", turns, "turns left")

        #---Determines whether the users guess is in the word that was randomly|
        #--- chosen then adds it to the list of correct letters in order ---#
        if guess in listW :
            indice =  [i for i, x in enumerate(listW) if x == guess]
            index = listW.index(guess)

            for i in indice:
                uLetters[i] = guess
            list = "".join(uLetters)

        elif guess in listWU :
            indice =  [i for i, x in enumerate(listWU) if x == guess]
            index = listW.index(guess.lower())

            for i in indice:
                uLetters[i] = guess.lower()
            list = "".join(uLetters)

        #--- Determines whether the user has inputted the correct full word and ends/finishes the game ---#
        if list == randomL and turns >= 0:
            print( "Letters Guessed:", " ".join(uLetters))
            print("you guessed all the correct letters with only",turns,"turns left\n\t\t\t the word was",randomL.upper())
            game = False
            break






#--- Displays the correct hangman image depending on how many turns the user has left ---#
        if turns == 8:
            print("___________.._______\n"
                 "| .__________))______|\n"
                 "| | / /      ||\n"
                 "| |/ /       ||\n"
                 "| | /        ||\n"
                 "| |/         |/\n"
                 "| |          \n"
                 "| |          \n"
                 "| |         \n"
                 "| |         \n"
                 "| |           \n"
                 "| |            \n"
                 "| |             \n"
                 "| |              \n"
                 "| |           \n"
                 "| |           \n"
                 "| |          \n"
                 "| |         \n"
                 "-----------------------\n"
                 "|                      |\n"
                 "-----------------------\n"
                 "^current status^", turns, "turns left")






        #--- Detects if the user guessed the full word in one answer ---#
        if guess == randomL or guess == randomL.upper():
            print("YOU SLY BASTARD, YOU GOT IT and only with",turns,"turns left the word was",randomL.upper())
            game = False
            break



        if turns <= 0 or list == randomL:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y/\n"
                  "| |       // |   | //\n"
                  "| |      //  | . |  //\n"
                  "| |     ')   |   |   (`\n"
                  "| |          ||'||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |         / | | /\n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n",)
            print("You lost, the word was",randomL)
            game = False
            break

        if turns == 1:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y/\n"
                  "| |       // |   | //\n"
                  "| |      //  | . |  //\n"
                  "| |     ')   |   |   (`\n"
                  "| |          ||'||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |         / |  \n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n",
                  "^current status^", turns, "turns left")

        if turns == 2:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y/\n"
                  "| |       // |   | //\n"
                  "| |      //  | . |  //\n"
                  "| |     ')   |   |   (`\n"
                  "| |          ||'||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |          || ||\n"
                  "| |           \n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n",
                  "^current status^", turns, "turns left")

        if turns == 3:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y/\n"
                  "| |       // |   | //\n"
                  "| |      //  | . |  //\n"
                  "| |     ')   |   |   (`\n"
                  "| |          ||'\n"
                  "| |          || \n"
                  "| |          || \n"
                  "| |          || \n"
                  "| |          \n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n"
                  "^current status^", turns, "turns left"
                  )
        if turns == 4:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y/\n"
                  "| |       // |   | //\n"
                  "| |      //  | . |  //\n"
                  "| |     ')   |   |   (`\n"
                  "| |              \n"
                  "| |           \n"
                  "| |           \n"
                  "| |          \n"
                  "| |         \n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n"
                  "^current status^", turns, "turns left"
                  )
        if turns == 5:
            print("___________.._______\n"
                  "| .__________))______|\n"
                  "| | / /      ||\n"
                  "| |/ /       ||\n"
                  "| | /        ||.-''.\n"
                  "| |/         |/  _  \n"
                  "| |          ||  `/,|\n"
                  "| |          (//`_.\n"
                  "| |         .-`--'.\n"
                  "| |        /Y . . Y\n"
                  "| |       // |   | \n"
                  "| |      //  | . |  \n"
                  "| |     ')   |   |   \n"
                  "| |              \n"
                  "| |           \n"
                  "| |           \n"
                  "| |          \n"
                  "| |         \n"
                  "-----------------------\n"
                  "|                      |\n"
                  "-----------------------\n"
                  "^current status^", turns, "turns left"
                  )
        if turns == 6:
            print("___________.._______\n"
                 "| .__________))______|\n"
                 "| | / /      ||\n"
                 "| |/ /       ||\n"
                 "| | /        ||.-''.\n"
                 "| |/         |/  _  \n"
                 "| |          ||  `/,|\n"
                 "| |          (//`_.\n"
                 "| |         .-`--'.\n"
                 "| |         Y . . Y\n"
                 "| |          |   | \n"
                 "| |          | . |  \n"
                 "| |          |   |   \n"
                 "| |              \n"
                 "| |           \n"
                 "| |           \n"
                 "| |          \n"
                 "| |         \n"
                 "-----------------------\n"
                 "|                      |\n"
                 "-----------------------\n"
                 "^current status^", turns, "turns left"
                  )
        if turns == 7:
            print("___________.._______\n"
                 "| .__________))______|\n"
                 "| | / /      ||\n"
                 "| |/ /       ||\n"
                 "| | /        ||.-''.\n"
                 "| |/         |/  _  \n"
                 "| |          ||  `/,|\n"
                 "| |          (//`_.\n"
                 "| |         .-`--'.\n"
                 "| |         \n"
                 "| |           \n"
                 "| |            \n"
                 "| |             \n"
                 "| |              \n"
                 "| |           \n"
                 "| |           \n"
                 "| |          \n"
                 "| |         \n"
                 "-----------------------\n"
                 "|                      |\n"
                 "-----------------------\n"
                 "^current status^", turns, "turns left"
                  )

        print("Correct Letters Guessed:", " ".join(uLetters), " All letters guessed:","[", " , ".join(LOUL),"]")

#--- When the turns are equal to 0 game is equal to false, the game ends and the user loses ---#
while game == False:

        break

##############


