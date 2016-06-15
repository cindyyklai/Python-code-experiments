# Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter.
# Assume your input is only one word containing no spaces or punctuation.
# No need to worry about score multipliers.
# Assume that you're only given non-empty strings.
    
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    total_score = 0
    for txt in word:
        total_score += score[txt.lower()]

    return total_score

print scrabble_score('cindy')