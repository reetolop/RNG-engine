from assets.Input_utilities import string_input, integer_input , yesno_input
from core.Number_generator import randomize_int



def compare(reference, target):
    if reference > target :
        return "Your colder"
    
    elif reference < target :
        return "Your warmer"
    


def again():
    play_again = yesno_input("Would you like to try again? y/n ")
    
    if not play_again: 
        return False
    


def play():

    start_up = True

    while start_up:

        min_num = integer_input("Enter the minimum number:  ")
        max_num = integer_input("Enter the maximum number:  ")
        roll = randomize_int(min_num, max_num)

        gt_lt = yesno_input("would you like it to tell you wether your hotter or colder? y/n:  ")    

        running = True

        
        
        while running:

            guess = integer_input(f"Enter your guess! Its a one in {(max_num - min_num)} chance:   ")

            match guess:

                case guess if guess not in range(min_num,max_num + 1):
                
                    print("You have entered a value outside of the selected range")
            
                case guess if guess == roll.chosen:
                    print("you guessed it")
                    break


                case guess if guess != roll.chosen and gt_lt:
                    print(f"{compare(roll.chosen, guess)} , try again")

                case guess if guess != roll.chosen and not gt_lt:
                    print("Too bad try again ")


        if  not again():
            print("Alright, have a great day!")
            start_up = False
        
        

if __name__ == "__main__":
    play()