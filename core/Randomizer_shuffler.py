import random 

class Randomized:
    
    class Randomize:

        def __init__ (self, items, ):
            self._result = None
            self._items = items
            #self.mode = mode

        def roll (self):
            self._result = random.choice(self._items)
            return self._result


        @property
        def result(self):
            if self._result is None:
                self.roll()
            return self._result
        
        def __str__(self):
            return f"{self.result} was rolled"



list1 = Randomized.Randomize(["apple", "banana" , "coconut"])
print(list1)
print(list1.result)