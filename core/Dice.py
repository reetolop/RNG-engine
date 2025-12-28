import random


# Data structure for dices
class Database:
    

    class RollData:

        count = 0
        full_total = 0

        def __init__(self,  dice_count, rolled, ):        #each roll will get its own object with its data on it

            self.dice_count = dice_count    # amount of dice that will get rolled
            self.rolled = rolled            # the numbers that the dices rolled 
            self.value = sum(rolled)        # the total of those rolled numbers
            Database.RollData.count += 1
            Database.RollData.full_total += self.value

        def __str__(self):
            rolled_str = "|".join(str(num) for num in self.rolled)     # will have to dissolve lists into str to use string methods
        
            return (
                f"Round {Database.RollData.count} - Dice Rolled: {self.dice_count}, "
                f"Rolls: {rolled_str}, Total: {self.value}"
            )                                                           # when we call a (roll) it returns all the data back

    average = 0
    median = 0 



    #roll and add the data into the database above 
    def add_roll(self,  add_count ):

        new_roll = self.RollData( add_count, [ random.randint(1,6) for _ in range(add_count)] )     # Rolls the dices according to the count 
        self.data_list.append(new_roll)


    def get_data(self):
        for data in self.data_list:
            print(data)
    # Return the data
    

    def __init__(self, name):
        self.name = name
        self.data_list = []

