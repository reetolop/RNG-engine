def string_input(string) -> str:
    
    while True:
        word: str = input(string).strip().lower()

        if any(char.isdigit() for char in word) or word != (""):
            print("Please do not enter numbers")

        else:
            print("please do not enter numbers or blanks")