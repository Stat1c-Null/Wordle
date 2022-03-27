import random as r
from colorama import Back, Style, Fore
#Possible words to guess
words = ["NYMPH", "PAPER", "HANDS", "CHALK", "toxic", "water", "epoxy"]
hidden_word = r.choice(words)#Word to guess

#Variables
lives = 6#Number of tries
wrong_letters = []
correct_letters = []#Used letters 
wrongpos_letters = []
ph = "*****"
guessed_words = []
#Functions
def print_words(word1, word2, word3, word4, word5, word6):
  print(Fore.BLUE + "\n\t\t\t\t" + word1 + "\n\t\t\t\t" + word2 + "\n\t\t\t\t" + word3 + "\n\t\t\t\t" + word4 + "\n\t\t\t\t" + word5 + "\n\t\t\t\t" + word6)

#Game Logic
print(Fore.GREEN + "\t\t\tWelcome to Wordle!" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "\n\t\tYou have 6 tries to guess a 5 letter word" + Style.RESET_ALL)

print_words(ph, ph, ph, ph, ph, ph)

guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL)

while len(guess) > 5 or len(guess) < 5:
  print(Fore.RED + "INVALID INPUT WORD MUST BE 5 LETTERS LONG")
  guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL)
