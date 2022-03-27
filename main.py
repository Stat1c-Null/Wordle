import random as r
from colorama import Back, Style, Fore
#Possible words to guess
words = ["NYMPH", "PAPER", "HANDS", "CHALK", "TOXIC", "WATER", "EPOXY"]
hidden_word = r.choice(words)#Word to guess
hidden_letters = []
for char in hidden_word:
  hidden_letters.append(char)

#Variables
lives = 6#Number of tries
counter = 0
wrong_letters = []
correct_letters = []#Used letters 
wrongpos_letters = []
temp = []
ph = "*****"
guessed_words = [ph, ph, ph, ph, ph, ph]
guess = ""
#Functions
def print_words(word1, word2, word3, word4, word5, word6):
  print(Fore.BLUE + "\n\t\t\t\t" + word1 + "\n\t\t\t\t" + word2 + "\n\t\t\t\t" + word3 + "\n\t\t\t\t" + word4 + "\n\t\t\t\t" + word5 + "\n\t\t\t\t" + word6 + "\n")

#Game Logic
print(Fore.MAGENTA + "\t\t\tWelcome to Wordle!" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "\n\t\tYou have 6 tries to guess a 5 letter word" + Style.RESET_ALL)

#Game Loop
while guess != hidden_word and lives > 0:
  print_words(guessed_words[0], guessed_words[1], guessed_words[2], guessed_words[3], guessed_words[4], guessed_words[5])
  print(hidden_word)

  print(Fore.GREEN + "Correct Letters:" + str(correct_letters))
  print(Fore.RED + "Wrong Letters:" + str(wrong_letters))
  guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL).upper()

  #Check if the guess length is correct
  while len(guess) > 5 or len(guess) < 5:
    print(Fore.RED + "INVALID INPUT WORD MUST BE 5 LETTERS LONG")
    guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL)
  #Split chars in guess

  #Compare chars
  print(temp)
  #Check if the guess is correct
  if guess == hidden_word:
    print(Back.GREEN + Fore.BLACK + "You have guess the word correctly!"+ Style.RESET_ALL)
    break
  else:
    print(Back.RED + Fore.BLACK + "Completely incorrect" + Style.RESET_ALL)
    lives -= 1
    guessed_words.insert(counter, guess)
    counter += 1
    for char in guess:
      wrong_letters.append(char)
    temp = []