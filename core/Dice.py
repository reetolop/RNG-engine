import random



# Data structure for dices
class Database:
    

    class RollData:
        def __init__(self, roll_num, dice_count, rolled, ):        #each roll will get its own object with its data on it

            self.roll_num = roll_num
            self.dice_count = dice_count
            self.rolled = rolled
            self.value = sum(rolled)
            

        def __str__(self):
            rolled_str = ", ".join(str(num) for num in self.rolled)     # will have to dissolve lists into str to use string methods
        
            return (
                f"Round {self.roll_num} - Dice Rolled: {self.dice_count}, "
                f"Rolls: {rolled_str}, Value: {self.value}"
            )                                                           # when we call a (roll) it returns all the data back


    #roll and add the data into the database above 
    def add_roll(self, add_num, add_count ):

        new_roll = self.RollData(add_num, add_count, [ random.randint(1,6) for x in range(add_count)] )     
        self.data_list.append(new_roll)


    def get_data(self):
        return [ print(x) for x in self.data_list]   # Return the data
    

    def __init__(self, name):
        self.name = name
        self.data_list = []



Main1 = Database("Main_data")

Main1.add_roll(2,5)

Main1.get_data()


