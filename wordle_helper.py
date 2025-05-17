import argparse
from os.path import dirname, join

def get_words_with_letters(letters):
    with open(join(dirname(__file__), 'targets.txt'), 'r') as f:
        words = f.read().splitlines()
    return [word for word in words if all(letter in word for letter in letters)]

parser = argparse.ArgumentParser(description="Wordle helper")
parser.add_argument('-u', '--used', type=str, required=False, default="", help="Used letters")
parser.add_argument('-t', '--hints', type=str, required=False, default="", help="Hints: letter place colour, comma-separated (e.g. a1g,b2y)")
parser.add_argument('-l', '--letters', type=str, required=False, default="", help="Letters to include in the word")
parser.add_argument('-n', '--notallowed', type=str, required=False, default="", help="Letters not allowed")
args = parser.parse_args()

letters_used = set(args.used.replace(" ", "").lower())
hints = args.hints.replace(" ", "").lower().split(",") if args.hints else ""
letters = list(set(args.letters)) + [hint[0] for hint in hints]
notallowed = args.notallowed or [l for l in letters_used if l not in letters]

def get_words_with_hints(hints):
    words = get_words_with_letters(letters)

    if not hints: return words

    return [word for word in words if all(
        (hint[2] != "y" or word[int(hint[1])-1] != hint[0]) and
        (hint[2] != "g" or word[int(hint[1])-1] == hint[0])
        for hint in hints)]

def filter(words, notallowed):
    return [word for word in words if all(letter not in word for letter in notallowed)]

x = get_words_with_hints(hints)

print(', '.join(filter(x, notallowed)))