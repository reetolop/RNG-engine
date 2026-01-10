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
        