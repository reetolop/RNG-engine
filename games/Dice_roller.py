from core import Dice

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
#spacing between the lines is also important because its using for loops to print the correct lines
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
        
        elif float(word) != ValueError:
            print("Please do no enter numbers")

        else:
            print("please enter a valid input and do not enter blanks")


#Display the dices
def display_dice(rolls): 
    for line in range(7):       # each dice has a height of 7 ( 7 lines height) , so we print 1 horizontal line each for 7 times
        for die in rolls:       # for die(placeholder) in what ever the rolled [list] of values of 
            print(dice_art[die][line], end="")    # print the horizontal line of the horizontal line were on 
        print()         # after were done printing the whole horizontal line of the display go onto the next

# Roll the dice(s)! 
def play(database):  #use a database the user created 


    print("Lets roll some dice shall we? ")
    round_num = -1
    while True:
        user_count = integer_input("How many dices would you like to roll?   ")
        round_num += 1
        database.add_roll(round_num + 1, user_count)  # add in all the values to create an object for the roll

        last_roll = database.data_list[-1].rolled    # get the last [list] of .rolled numbers from the main database
        display_dice(last_roll)                  # put that into the display function 

        print(database.data_list[-1])                # print the whole data (summary)




if __name__ == "__main__":

    Main = Dice.Database("main")
    play(Main)

