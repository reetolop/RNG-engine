import random
from typing import List
from .session_stats import SessionStats


# Data base
class Database:
    

    def __init__(self, name):       
        self.name: str = name
        self.data_list: List[Database.RollData] = []      # stores all objects (roll data)
        self.stats = SessionStats()


    class RollData:

        def __init__(self, round_number , dice_count: int, rolled: List[int], ):        #each roll will get its own object with its data on it
            
            self.round_number = round_number           
            self.dice_count: int = dice_count          # amount of dice that will get rolled in this round
            self.rolled: List[int] = rolled            # result of the dices 

            self.value: int = sum(rolled)                     # the total of this round
            self.average: float = self.value / dice_count      # average for this round




        def __str__(self) -> str:
            rolled_str = "|".join(str(num) for num in self.rolled)     # will have to dissolve lists into str to use string methods
        
            return (
                f"Round { self.round_number } - Dice Rolled: {self.dice_count}  "
                f"Rolls: {rolled_str}  Total: {self.value}  Average: {self.average: .2f}"
            )                                                           


    
    def add_roll(self,  dice_count: int ) -> None:

        
        rolled = [ random.randint(1,6) for _ in range(dice_count)]     # Rolls the dices according to the count 
        roll = self.RollData(self.stats._count, dice_count, rolled)
        self.stats.update( dice_count, roll.value, rolled)
        self.data_list.append(roll)



    def get_data(self) -> None:
        for data in self.data_list:
            print(data)
            