def string_input(string):
    while True:
        word = input(string).strip().lower()

        if word != (""):
            return word 
        
        elif float(word) != ValueError:
            print("Please do not enter numbers")

        else:
            print("please enter a valid input and do not enter blanks")