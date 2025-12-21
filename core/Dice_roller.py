import random

("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")  
#  ● ┌ ─ ┐ │ └ ┘  Ascii art for the dice(s)

"┌───────────────┐"
"│               │"
"│               │"
"│               │"
"│               │"
"│               │"
"└───────────────┘"


#Have a dice art dict to have a key value relation between the dice art and the number itself
#spacing between the lines is also important because its using for loops to print the correct line
dice_art = {

    1: ("┌───────────────┐",
        "│               │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│               │",
        "└───────────────┘"),



    2: ("┌───────────────┐",
        "│    ●          │",
        "│               │",
        "│               │",
        "│               │",
        "│          ●    │",
        "└───────────────┘"),



    3: ("┌───────────────┐",
        "│    ●          │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│          ●    │",
        "└───────────────┘"),



    4: ("┌───────────────┐",
        "│    ●     ●    │",
        "│               │",
        "│               │",
        "│               │",
        "│    ●     ●    │",
        "└───────────────┘"),



    5: ("┌───────────────┐",
        "│    ●     ●    │",
        "│               │",
        "│       ●       │",
        "│               │",
        "│    ●     ●    │",
        "└───────────────┘"),



    6: ("┌───────────────┐",
        "│    ●     ●    │",
        "│               │",
        "│    ●     ●    │",
        "│               │",
        "│    ●     ●    │",
        "└───────────────┘"),

}

# all global constants , i tried my best to data model efficiently 

dice_num = 0
totals = {"roll_count": 0 ,  # counter to track the number of rolls its into ( also use it as a counter for loops)
          "dice_rolled" : [ ],  # list to put the number of dice rolled for each round 
          "dice_value" : [ ],    # The total with the dices for each round
          "full_total" : 0,    # get all the total of the dices rolled 
          "total": 0,     # total amount of dice rolled    
          }




#Reusable integrated int converter/checker for input
def integer_input(number):
    while True: 
        num = input(number).strip()

        try:
            return int(num)
        
        except ValueError:
            print("Please enter numbers only")
            continue

# same for strings
def string_input(string):
    while True:
        word = input(string).strip().lower()

        if word not in ("",):
            return word 
        else:
            print("please enter a valid input and do not enter blanks")




# Roll function
def roll():
    dice_num = integer_input("Enter the amount of dices:    ")
    totals["dice_rolled"].append(dice_num)

    #Roll the dices 
    totals["dice_value"].clear()
    for die in range(dice_num):
        totals["dice_value"].append(random.randint(1,6))

    print(f"Roll {totals["roll_count"]}")

    #Display the dices 

    for line in range(7):           #1 dice art has 7 total spaces(line length) , print those horizontal line by line (--- --- --- ) also have to get the correct dice line that was rolled 
        for die in totals["dice_value"]:            # for every die(placeholder) in dice [] that was rolled 
            print(dice_art.get(die)[line], end= "")   # get the index for each dice rolled (ex 2 5 3 ) then print each of the horizontal line for the dice 
            #ex) if first index of dice[] was 2 , get the  horizontal line of 2 and then print it , then so on 
        print() # go to next horizontal line after printing out 1 of the horizontal line 




    total = sum(totals["dice_value"])
    print(f"Total amount with the dices is {total}")




print("Lets roll some dice shall we?")
roll()

while True:

    reroll = string_input("Would you like to reroll?(y/n)    ")

    if reroll in("y", "yes"):
        roll()
        continue
    elif reroll in("n", "no"):
        break
    
    else:
        print("please enter yes or no only")
        continue

