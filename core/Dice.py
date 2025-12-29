import random
from collections import Counter
from assets.Sorting import quick_sort





# Data base
class Database:
    

    def __init__(self, name):       
        self.name = name
        self.data_list = []         # every single data will be stored in this list (as a tuple)
                                                                        # although its not stored as a tuple now i will change it to do so when i add a check history feature


    class RollData:

        count = 0           # roll count (round)
        full_dice = 0       # total number of dices rolled
        full_total = 0      # total of all the numbers that the dices rolled
        average = 0         # average number rolled from all dices 

        value_list = []     # to track all the numbers rolled
        sorted_list = None  # placeholder for the sorted list we will use for getting statistics


        def __init__(self,  dice_count, rolled, ):        #each roll will get its own object with its data on it

            self.dice_count = dice_count    # amount of dice that will get rolled
            self.rolled = rolled            # the numbers that the dices rolled

            self.value = sum(rolled)        # the total of those rolled numbers
            self.average = self.value/ dice_count      # the average number for the round (roll count )

            
            Database.RollData.value_list.extend(rolled)         #record all the rolled numbers (used for statistics later)
            Database.RollData.count += 1                        #counts the roll count(round) , used as a counter 
            Database.RollData.full_dice += dice_count
            Database.RollData.full_total += self.value          
            Database.RollData.average = Database.RollData.full_total / Database.RollData.full_dice      #calculates then updates the average (Whole session)




        def __str__(self):
            rolled_str = "|".join(str(num) for num in self.rolled)     # will have to dissolve lists into str to use string methods
        
            return (
                f"Round {Database.RollData.count} - Dice Rolled: {self.dice_count}  "
                f"Rolls: {rolled_str}  Total: {self.value}  Average: {self.average}"
            )                                                           # when we call (roll) it returns all the data back 



        @classmethod
        def get_total(cls):
            return cls.full_total         #cls method for getting the all time total


        @classmethod
        def get_average(cls):
            return f"{cls.average :.2f}"            #cls method for getting the average number rolled
            

        @classmethod
        def sort_value(cls):                               #sort all the numbers rolled in order using quick sort
            if cls.sorted_list is None :
                cls.sorted_list = quick_sort(cls.value_list)
            return cls.sorted_list
        

        @classmethod
        def calculate_median(cls):
            if cls.sorted_list is None:
                cls.sorted_list = quick_sort(cls.value_list)                               
    
            n = len(cls.sorted_list)

            if n == 0: return None 

            mid = n // 2 

            return cls.sorted_list[mid] if n % 2 else (cls.sorted_list[mid - 1] + cls.sorted_list[mid]) / 2

        
        @classmethod
        def calculate_mode(cls):
            if not cls.value_list:
                return None

            counts = Counter(cls.value_list)
            max_freq = max(counts.values())
            modes = [num for num , freq in counts.items() if freq == max_freq]

            return modes if len(modes) > 1 else modes[0]
 


    #roll and add the data into the database above 
    def add_roll(self,  add_count ):

        new_roll = self.RollData( add_count, [ random.randint(1,6) for _ in range(add_count)] )     # Rolls the dices according to the count 
        self.data_list.append(new_roll)



    def get_data(self):
        for data in self.data_list:
            print(data)
    # Return the data (for each round , NOT Stats)
    
