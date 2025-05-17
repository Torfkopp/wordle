import random
from os.path import dirname, join
from robo import Robo

amount = input("Amount of games to play: ")
wins, losses = [], 0

with open(join(dirname(dirname(__file__)), "targets.txt"), "r") as f:
    targets = f.read().splitlines()

for i in range(int(amount)):
    
    robo = Robo()
    word = random.choice(targets)
    
    finished, i = False, 0

    while not finished and i < 5:
        guess = robo.guess_word()

        i += 1

        if guess == word:
            finished = True
            break

        result = ""
        for j in range(5):
            if guess[j] == word[j]:
                result += "✓"
            elif guess[j] in word:
                result += "0"
            else:
                result += "✕"

        robo.get_result(result)

    if finished:
        wins.append(i)
        #print("Word guessed!")
    else:
        losses += 1
        #print("Lost! The word was: " + word)

print(f"Wins: {len(wins)}, Losses: {losses}")
print(f"Average guesses: {sum(wins) / len(wins):.2f}" if wins else "Average guesses: 0")
print(f"Winrate: {len(wins) / (len(wins) + losses) * 100:.2f}%")