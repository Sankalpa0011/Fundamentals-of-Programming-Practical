#4. Write a program to input a word and pick a character from it randomly and display it.

import random

word = str(input('Enter random word: '))
randomone = random.randint(0,len(word)-1)
randomcharacter = word[randomone]

print('The picked random character: ',randomcharacter)
