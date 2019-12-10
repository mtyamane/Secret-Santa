#-----
# Author: Mark Yamane
# This program is used to generate names or create lists of name-pairs for secret santa
# Note: names are not case-sensitive and people will never pull themselves
#-----

from random import randint
from os import system, name
from time import sleep
import sys

def resetLists(people):
    santas = list.copy(people)
    giftees = list.copy(people)
    listDict = {k:[] for k in people}
    return santas, giftees, listDict;

# Loop to simulate pulling names
def namePull(santa, santaIndex, santas, giftee, giftees, listDict):
    while giftee == santa:
        giftIndex = randint(0, (len(giftees)-1))
        
        # prevent last person from choosing themself
        if len(giftees) == 2 and giftees[1-giftIndex] == santas[1-santaIndex]:
            giftIndex = 1 - giftIndex
        elif len(giftees) == 1:
            giftIndex = 0
        giftee = giftees[giftIndex]
    listDict[santa] = giftee
    del(santas[santaIndex])  # this santa is no longer able to pull a name
    del(giftees[giftIndex])  # this name is no longer able to be selected
    
    return santa, santaIndex, santas, giftee, giftees, listDict;

# Optional program restart
def redoPulls():
    again = input("Run the program again? (y/n): ")
    while again != "y" and again != "n":
        print("Invalid input, try again.")
        again = input("Run the program again? (y/n): ").lower()
    if again == "y":
        print()
        secretSanta()

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

# The name drawing!
def secretSanta():
    people = ["name1", "name2", "name3"]  # replace these for the specific game of Secret Santa
    people = [n.lower() for n in people]  # formats list of people
    peopleSanta, peopleAssigned, listDict = resetLists(people)
    
    # legend
    print("l = create a list")
    print("p = pull names individually")
    print("q = quit the program")
    
    ver = input("Create a list or pull names? ").lower()
    while ver != "l" and ver != "p" and ver != "q":
        print("Invalid input, try again.")
        ver = input("Create a list or pull names? ").lower()
    
    # create a list of name-pairs
    if ver == "l":
        while len(peopleAssigned) is not 0:
            santaIndex = randint(0, (len(peopleSanta)-1))
            santa = peopleSanta[santaIndex]
            giftee = santa
            
            santa, santaIndex, peopleSanta, giftee, peopleAssigned, listDict = namePull(santa, santaIndex, peopleSanta, giftee, peopleAssigned, listDict)
        print()
        # print the list of names
        for person, gift in listDict.items():
            print(person.capitalize(), ": ", gift.capitalize(), sep = "")
        print()
        redoPulls()
    
    # pull names individually
    elif ver == "p":
        print()
        while len(peopleAssigned) is not 0:
            santaIndex = 0
            # optional legend
            # print("r = restart program")
            # print("q = quit the program")
            santa = input("Type your name: ").lower()
            while santa not in peopleSanta:
                if santa == "q":
                    sys.exit("Quitting the program...")
                elif santa == "r":
                    screen_clear()
                    print("Starting secret santa over...")
                    peopleSanta, peopleAssigned, listDict = resetLists(people)
                elif santa in people:
                    print("You have already been assigned a person, try another name.")
                else:
                    print("Invalid input, try again.")
                santa = input("Type your name: ").lower()
            # find index of this santa
            while santa != peopleSanta[santaIndex]:
                santaIndex += 1
            giftee = santa
            giftIndex = 0
            
            santa, santaIndex, peopleSanta, giftee, peopleAssigned, listDict = namePull(santa, santaIndex, peopleSanta, giftee, peopleAssigned, listDict)
            print ("Get a present for:", giftee.capitalize())
            sleep(2)  # give time for the santa to process their giftee
            screen_clear()  # so that the next person will not see previous assignments
        print ("All recipients have been assigned!")
        sleep(2)
        
        check = input("Check the list? (y/n): ")
        if check == "y":
            # print the list of names
            for person, gift in listDict.items():
                print(person.capitalize(), "should get a present for", gift.capitalize())
            sleep(4)
        redoPulls()
    
secretSanta()
print ("All done!")
