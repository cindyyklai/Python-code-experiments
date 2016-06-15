# A function that takes one string, text, as input and returns the text with all of the vowels removed.
#
# For example: anti_vowel("Hey You!") should return "Hy Y!".
# Make sure to remove lowercase and uppercase vowels.

def anti_vowel(text):
    for t in text:
        if t in "aeiouAEIOU":
            text = text.replace(t, '')
    return text

print anti_vowel('cindy')