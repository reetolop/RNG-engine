def yesno_input(string) -> bool:
    while True:
        word: str = input(string).strip().lower()

        if any([char.isdigit() for char in word]):
            print("Please do not enter numbers")

        else:
        
            if word != ("") and word in("y", "yes",):
                return True
            

            elif word != ("") and word in ("n", "no"):
                return False
                
            else:
                print("please enter yes or no")
                


