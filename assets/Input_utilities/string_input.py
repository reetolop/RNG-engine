def string_input(string):
    while True:
        word = input(string).strip().lower()

        if word != (""):
            return word 
        
        if any([char.isdigit for char in word]):
            print("Please do not enter numbers")

        else:
            print("please do not enter numbers or blanks")