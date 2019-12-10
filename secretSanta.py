#-----
# Author: Mark Yamane
# This program is used to generate names for secret santa
# Note: names are not case-sensitive and people will never pull themselves
#-----

from random import randint
from os import system, name
from time import sleep
import sys

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

def secretSanta():
    people = ["name1", "name2", "name3"]  # replace these for the specific game of Secret Santa
    people = [n.lower() for n in people]  # formats list of people
    peopleSanta = list.copy(people)
    peopleAssigned = list.copy(people)
    listDict = {k:[] for k in people}

    # legend
    print("l = create a list")
    print("p = pull names individually")
    print("q = quit the program")

    ver = input("Create a list or pull names? ").lower()
    while ver != "l" and ver != "p" and ver != "q":
        print("Not a valid input, try again.")
        ver = input("Create a list or pull names? ").lower()

    # to create a list of name-pairs
    if ver == "l":
        while len(peopleAssigned) is not 0:
            santaIndex = randint(0, (len(peopleSanta)-1))
            santa = peopleSanta[santaIndex]
            giftee = santa
            giftIndex = 0

            # find a different person's name
            while giftee == santa:
                giftIndex = randint(0, (len(peopleAssigned)-1))

                # prevent last person from choosing themself
                if len(peopleAssigned) == 2 and peopleAssigned[1-giftIndex] == peopleSanta[1-santaIndex]:
                    giftIndex = 1 - giftIndex
                elif len(peopleAssigned) == 1:
                    giftIndex = 0

                giftee = peopleAssigned[giftIndex]

            listDict[santa] = giftee

            del(peopleSanta[santaIndex])  # this santa is no longer able to pull a name
            del(peopleAssigned[giftIndex])  # this name is no longer able to be selected
        print()

        # print the list of names
        for person, gift in listDict.items():
                print(person.capitalize(), ": ", gift.capitalize(), sep = "")
        print()
        again = input("Run the program again? (y/n): ")
        if again == "y":
            print()
            secretSanta()

    # to pull names individually
    elif ver == "p":
        print()
        while len(peopleAssigned) is not 0:
            santaIndex = 0
            print("r = restart program")
            print("q = quit the program")
            santa = input("Type your name: ").lower()
            while santa not in peopleSanta:
                if santa == "q":
                    sys.exit("Quitting the program...")
                elif santa == "r":
                    screen_clear()
                    print("Starting secret santa over...")
                    peopleSanta = list.copy(people)
                    peopleAssigned = list.copy(people)
                    listDict = {k:[] for k in people}
                elif santa in people:
                    print("You have already been assigned a person, try another name.")
                else:
                    print("This name is not a valid santa, try another one.")
                santa = input("Type your name: ").lower()
            while santa != peopleSanta[santaIndex]:
                santaIndex += 1
            giftee = santa
            giftIndex = 0

            # find a different person's name
            while giftee == santa:
                giftIndex = randint(0, (len(peopleAssigned)-1))

                # prevent last person from choosing themself
                if len(peopleAssigned) == 2 and peopleAssigned[1-giftIndex] == peopleSanta[1-santaIndex]:
                    giftIndex = 1 - giftIndex
                elif len(peopleAssigned) == 1:
                    giftIndex = 0

                giftee = peopleAssigned[giftIndex]

            print ("Get a present for:", giftee.capitalize())

            listDict[santa] = giftee

            del(peopleSanta[santaIndex])  # this santa is no longer able to pull a name
            del(peopleAssigned[giftIndex])  # this name is no longer able to be selected
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
        again = input("Run the program again? (y/n): ")
        if again == "y":
            print()
            secretSanta()

secretSanta()
print ("All done!")