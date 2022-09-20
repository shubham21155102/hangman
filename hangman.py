import random as rd
import hangman_logo as logo
import hangman_words as random_word
print(logo.logof)
choosen_word=rd.choice(random_word.word)
# print(choosen_word)
display=[]
for i in range(len(choosen_word)):
    display+="_"
# print(display)
end_of_game=False
# def newEntry(words):
#     words=input("Please guess any word:\n").lower()
# words=""
lives=6
while not end_of_game:
    words=input("Please guess any word:\n").lower()
    if words not in choosen_word:
        lives=lives-1
        print(logo.stages[lives])
        if lives==0:
            end_of_game=True
            print("You Loose")
    for i in range(len(choosen_word)):
        if words==choosen_word[i]:
            display[i]=words
    if "_" not in display:
            end_of_game=True
            print("Hello bruh You won")


    print(display)


