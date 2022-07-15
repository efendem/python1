import random
from uzwords import words
def get_word():
    word random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
        return word.upper()
def get_word():
            word=random.choice(words)
            return word.upper()

def display(user_letters, word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter+=letter
        else: 
                display_letter+="-"
                return display_letter

def play():
    word=get_word()

    word_letters=set(word)
    print(f"Men{len(word)} xonali son o'yladim. Topa olasizmi?")
    while len(word_letters)>0:
        print (display(user_letters, word))
        if len(user_letters)>0:
            print("shu vaqtgacha kiritgan harflaringiz")
