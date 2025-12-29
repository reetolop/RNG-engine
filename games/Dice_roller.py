#This Dice roller is inspired by Bro Code, please check out his channel!


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
            int(num)
        
        except ValueError:
            print("Please enter numbers only")
            continue

        else: 
            return int(num)
        


# same for strings
def string_input(string):
    while True:
        word = input(string).strip().lower()

        if word != (""):
            return word 
        
        elif float(word) != ValueError:
            print("Please do not enter numbers")

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
    while True:
        user_count = integer_input("How many dices would you like to roll?   ")
        database.add_roll(user_count)  # add in all the values to create an object for the roll

        last_roll = database.data_list[-1].rolled    # get the latest [list] of .rolled numbers from the main database
        display_dice(last_roll)                  # put that into the display function 

        print(database.data_list[-1])               # print the whole data (summary) , also latest


        while True:
            Check_status = string_input("Do you want to see the statistics for this session? y/n" )         #ask to check stats
            if Check_status in {"y", "yes"}:
                see_statistics(database)
                break

            elif Check_status in {"n", "no"}:
                print("To the next round!")
                break

            else:
                print("Please enter Yes or No")

        


def see_statistics(database):       #get statistics such as session total , average , median , modes and whatever

    print()
    print("Session Statistics")
    print()
    print(f"Dices Rolled: {database.RollData.full_dice}")
    print(f"Full session number total: {database.RollData.full_total}")
    print(f"average: {database.RollData.average: .3f}")
    print(f"Median:{database.RollData.calculate_median()}")
    print(f"Mode: {database.RollData.calculate_mode()}")




if __name__ == "__main__":

    Main = Dice.Database("main")
    play(Main)          #use the main database that was created 