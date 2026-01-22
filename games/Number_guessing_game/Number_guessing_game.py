from assets.Input_utilities import string_input, integer_input , yesno_input
from core.Number_generator import randomize_int
from Database_stats import database



def compare(reference, target):
    if reference > target :
        return "You're colder"
    
    elif reference < target :
        return "You're warmer"
    

def again():
    play_again = yesno_input("Would you like to try again? y/n ")
    return play_again
    


def play():

    start_up = True
    data = database()

    while start_up:
        
        print("\n Number guessing game \n")
        
        min_num = integer_input("Enter the minimum number:  ")
        max_num = integer_input("Enter the maximum number:  ")
        roll = randomize_int(min_num, max_num)
        range_size = abs(max_num - min_num) + 1 

        gt_lt = yesno_input("would you like it to tell you wether your hotter or colder? y/n:  ")    

        running = True

        
        
        while running:

            guess = integer_input(f"Enter your guess! Its a one in {range_size} chance:   ")

            data.attempts += 1
            data.guesses.append(guess)

            match guess:

                case guess if guess not in range(min_num,max_num + 1):
                
                    print("You have entered a value outside of the selected range")
            
                case guess if guess == roll.chosen:
                    print(f"you guessed it! The answer was {roll.chosen}")
                    print(data)
                    break


                case guess if guess != roll.chosen and gt_lt:
                    print(f"{compare(roll.chosen, guess)} , try again")

                case guess if guess != roll.chosen and not gt_lt:
                    print("Too bad try again ")


        if not again():
            print("Alright, have a great day!")
            start_up = False
        
        

if __name__ == "__main__":
    play()