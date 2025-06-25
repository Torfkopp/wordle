"Trying to use every letter but those used in the solution of the wordle"
import collections

VOCALS = "aeiou"
not_to_use = "comfy"

def filter_words(possibilities, not_to_use):
    filtered = []
    for word in possibilities:
        if not any(letter in word for letter in not_to_use):
            filtered.append(word)
    return filtered

def only_one_vocal(word):
    return sum(1 for letter in word if letter in VOCALS) < 2

def no_repeated_letters(word):
    return len(set(word)) == len(word)

depth_to_letter = {
    0: 'qu',
    1: 'j',
    2: 'z',
}

def find_wordlist(depth, wordlist):
    if depth >= 4: return wordlist
    if len(wordlist) - len(set(wordlist)) > 4: return wordlist
    # list of letters in wordlist removing vocals
    letters = set(''.join(wordlist)) - set(VOCALS)
    filtered = [word for word in filter_words(filtered_words, letters) if no_repeated_letters(word) and (depth_to_letter[depth] in word if depth < 3 else True)]
    
    for word in filtered:
        found_list = find_wordlist(depth + 1, wordlist + word)
        if len(set(found_list)) > 20: 
            wordlist = found_list
            break
    
    return wordlist


with open("game/wordles_possible.txt", "r") as f:
    words = f.read().splitlines()

with open("targets.txt", "r") as f:
    used = f.read().splitlines()

possibilities = words + used

filtered_words = filter_words(possibilities, not_to_use)

with open("game/letter_count.txt", "r") as f:
    letter_count = f.read().splitlines()

filtered_vocal_words = [word for word in filtered_words if 'x' in word and no_repeated_letters(word) and only_one_vocal(word)]

wordlist = []
for word in filtered_vocal_words:
    wordlist.append(find_wordlist(0, word))

best_words = max(wordlist, key=lambda x: len(set(x)))
print("Best words:", best_words)
