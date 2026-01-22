import random


class randomize_int:

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        
        self.chosen = random.randint(self.min_val, self.max_val)