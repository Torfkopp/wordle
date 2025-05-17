import random
from os.path import dirname, join

class Robo:

    def __init__(self):
        # with open(join(dirname(__file__), "wordles_possible.txt"), "r") as f:
        #     wordles = f.read().splitlines()
        
        with open(join(dirname(dirname(__file__)), "targets.txt"), "r") as f:
            targets = f.read().splitlines()

        self.wordles = targets #+ wordles
        self.letters_used = set()
        self.hints = set()
        self.letters = set()
        self.notallowed = set()
        self.last_guess = ""
        self.starting_sequence = ["clint", "soare"]

    def filter_letters(self):
        self.wordles = [word for word in self.wordles if all(letter in word for letter in self.letters)]
    
    def filter_notallowed(self):
        self.wordles = [word for word in self.wordles if all(letter not in word for letter in self.notallowed)]
    
    def filter_hints(self):
        self.wordles = [word for word in self.wordles if all(
            (hint[2] != "y" or word[int(hint[1])-1] != hint[0]) and
            (hint[2] != "g" or word[int(hint[1])-1] == hint[0])
            for hint in self.hints)]

    def guess_word(self):
        if self.starting_sequence:
            choice = self.starting_sequence.pop(0)
        else:
            choice = random.choice(self.wordles)
        self.last_guess = choice
        self.letters_used.update(choice)
        return choice
    
    def convert_to_hints(self, result):
        for i, c in enumerate(result):
            if c == "✓": self.hints.add(self.last_guess[i] + str(i+1) + "g")
            elif c == "0": self.hints.add((self.last_guess[i] + str(i+1) + "y"))

    def get_result(self, result):
        self.convert_to_hints(result)
        self.letters = set([hint[0] for hint in self.hints])
        self.notallowed = set([l for l in self.letters_used if l not in self.letters])
        self.filter_letters()
        self.filter_hints()
        self.filter_notallowed()
