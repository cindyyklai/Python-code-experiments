# A function that takes a string textand returns that string in reverse.
# For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with this.
# You may get a string containing special characters (for example, !, @, or #).
def reverse(text):
    new_str = ""
    print len(text)-1
    for i in range(len(text)-1, -1, -1):
        print text[i]
        new_str += text[i]
    return new_str