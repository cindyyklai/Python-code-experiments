def censor(text, word):
    new = text.replace(word, "*" * len(word))
    return new
print censor("my name is cindy","cindy")