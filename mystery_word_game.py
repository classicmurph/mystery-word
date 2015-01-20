import random

with open("/usr/share/dict/words") as w:
    word_list = w.readlines()

def mystery_word():
    mystery_word = random(word_list)
    print("The word has {} letters.".format(len(mystery_word)))
