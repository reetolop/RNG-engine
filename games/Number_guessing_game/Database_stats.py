

class database:
    
    def __init__(self):
        
        self.guesses = []
        self.attempts = 0

    def __str__(self):

        return f"Attempts: {self.attempts}, Your guesses: {self.guesses}"