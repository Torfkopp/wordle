import random
from os.path import dirname, join

class bcolors:
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'

from robo import robo
robo = None #robo()

with open(join(dirname(__file__),  "wordles_possible.txt"), "r") as f:
    wordles = f.read().splitlines()

with open(join(dirname(dirname(__file__)), "targets.txt"), "r") as f:
    targets = f.read().splitlines()

wordles = wordles + targets
word = random.choice(targets)

finished, i = False, 0

while not finished and i < 5:
    if not robo:
        guess = input("Guess: ").lower()
    else: 
        guess = robo.guess_word()
        print("Guess: " + guess)
        
    if len(guess) != 5:
        print("Please enter a 5 letter word.")
        continue
    if guess not in wordles:
        print("Please enter a valid word.")
        continue

    i += 1
    if guess == word:
        finished = True
        break

    result = ""
    for j in range(5):
        if guess[j] == word[j]:
            result += bcolors.GREEN + "✓" + bcolors.ENDC if not robo else "✓"
        elif guess[j] in word:
            result += bcolors.YELLOW + "0" + bcolors.ENDC if not robo else "0"
        else:
            result += "✕"
    
    if robo: robo.get_result(result)
    print(result)

if finished:
    print("You guessed the word!")
else: 
    print("You lost! The word was: " + word)