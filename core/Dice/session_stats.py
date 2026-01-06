from collections import Counter
from assets.Sorting import quick_sort
from typing import List, Union



class SessionStats:



    def __init__(self):

        self._count = 1                                          # number of rounds rolled
        self._full_dice = 0                                      # total number of dices rolled across all rounds
        self._full_total = 0                                     # sum of all dice values across all rounds
        self._value_list: List[int] = []                         # all individual dice values rolled 
        self._sorted_list: Union[List[int], None] = None         # cached sorted list for statistics


    def update(self, dice_count: int, roll_total: int, rolled: List[int]):

        self._count += 1
        self._full_dice += dice_count
        self._full_total += roll_total
        self._value_list.extend(rolled)
        self._sorted_list = None  # Invalidate cache


    def reset(self):

        self._count = 0
        self._full_dice = 0
        self._full_total = 0
        self._value_list.clear()
        self._sorted_list = None


    @property
    def count(self) -> int:
        return self._count


    @property
    def total(self) -> int:
        return self._full_total
    
    @property
    def dices(self) -> int:
        return self._full_dice
    

    # average value across all dice rolled in the session
    @property
    def average(self) -> float:
        return self._full_total / self._full_dice if self._full_dice else 0.0


    # sorted using quick sort
    @property
    def sorted_values(self) -> List[int]:
        if self._sorted_list is None:
            self._sorted_list = quick_sort(self._value_list)
        return self._sorted_list    # type: ignore


    @property
    def median(self) -> Union[float, None]:
        sorted_vals = self.sorted_values
        n = len(sorted_vals)
        if n == 0:
            return None
        mid = n // 2
        return sorted_vals[mid] if n % 2 else (sorted_vals[mid - 1] + sorted_vals[mid]) / 2


    @property
    def mode(self) -> Union[int, List[int], None]:
        if not self._value_list:
            return None
        counts = Counter(self._value_list)
        max_freq = max(counts.values())
        modes = [num for num, freq in counts.items() if freq == max_freq]
        return modes if len(modes) > 1 else modes[0]