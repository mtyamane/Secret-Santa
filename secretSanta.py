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

def generateReceipt(listDict):
    receipt = input("Do you want a receipt of the list? (y/n): ").lower()
    while receipt != "y" and receipt != "n":
        print("Invalid input, try again.")
        receipt = input("Do you want a receipt of the list? (y/n): ").lower()
    if receipt == "y":
        year = input("What year is this for: ")
        with open("secret-santa_"+year+".txt","w+") as f:
            # print the list of names
            f.write("Santa: Giftee\n")
            for person, gift in listDict.items():
                f.write(person.capitalize() + ": " + gift.capitalize() + "\n")
            f.close()

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
    with open("names.txt", "r") as f:
        names = f.readlines()  # replace these for the specific game of Secret Santa
        people = [n.lower().strip() for n in names]  # formats list of people
        santas, giftees, listDict = resetLists(people)
        f.close()

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
        while len(giftees) is not 0:
            santaIndex = randint(0, (len(santas)-1))
            santa = santas[santaIndex]
            giftee = santa

            santa, santaIndex, santas, giftee, giftees, listDict = namePull(santa, santaIndex, santas, giftee, giftees, listDict)
        print()
        # print the list of names
        for person, gift in listDict.items():
            print(person.capitalize(), ": ", gift.capitalize(), sep = "")
        print()
        generateReceipt(listDict)
        redoPulls()

    # pull names individually
    elif ver == "p":
        print()
        while len(giftees) is not 0:
            santaIndex = 0
            # optional legend
            # print("r = restart program")
            # print("q = quit the program")
            santa = input("Type your name: ").lower()
            while santa not in santas:
                if santa == "q":
                    sys.exit("Quitting the program...")
                elif santa == "r":
                    screen_clear()
                    print("Starting secret santa over...")
                    santas, giftees, listDict = resetLists(people)
                elif santa in people:
                    print("You have already been assigned a person, try another name.")
                else:
                    print("Invalid input, try again.")
                santa = input("Type your name: ").lower()
            # find index of this santa
            while santa != santas[santaIndex]:
                santaIndex += 1
            giftee = santa
            giftIndex = 0

            santa, santaIndex, santas, giftee, giftees, listDict = namePull(santa, santaIndex, santas, giftee, giftees, listDict)
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
            sleep(2)
        redoPulls()

secretSanta()
print ("All done!")
