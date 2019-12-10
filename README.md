# Secret-Santa
A program to pull names or create a list of name-pairs, originally written for secret santa.

**Note:** Names are not case-sensitive and people will not pull their own name.

## Installation Instructions
Find **secretSanta.py** on your computer

Replace name placeholders with names of people in your Secret Santa

## Running the Program
Open Command Prompt (Windows) or Terminal (MacOS) and go to **Secret-Santa** directory
```
python secretSanta.py
```
A prompt will appear with the following commands:
| Command | Purpose                                                                   |
| ------- | ------------------------------------------------------------------------- |
| l       | create a list of name-pairs                                               |
| p       | used to simulate pulling names out of a hat; will ask for names as inputs |
| q       | quit the program                                                          |
| r       | restart the program                                                       |

**For creating lists:** The program will automatically create a list of name-pairs using names set in the program.

**For pulling names:** The program will allow two seconds to read your person before clearing the screen and asking for the next name; names are not case-sensitive. Offers the option of checking the list of name-pairs.
