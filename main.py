import random as r
from colorama import Back, Style, Fore
import os, requests
#Possible words to guess
url = "http://www.mieliestronk.com/corncob_lowercase.txt"
words = requests.get(url)#Get dictionary from web
words = words.text.splitlines()#Splitting dictionary by words
#Sort through words
sorted_list = []
for i in range(len(words)):
  if len(words[i]) == 5:
    words[i] = words[i].upper()
    sorted_list.append(words[i])
  else:
    pass
hidden_word = r.choice(sorted_list)#Word to guess
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

#Check if the letter is already in list
def check_in_list(list1, counter, list2):
  if list1[counter] in list2:
    pass
  else:
    list2.append(list1[counter])

def compare_letters(cor_list, guess_list):
  global correct_letters, wrong_letters, wrongpos_letters
  cor_let = 0
  for z in range(len(cor_list)):
    if cor_list[z] == guess_list[z]:#Letter at exact position
      cor_let += 1
      check_in_list(guess_list, z, correct_letters)
    #Correct letter at wrong pos
    elif guess_list[z] in cor_list and guess_list[z] != cor_list[z]:
      #Check if letter is in the word but not at the right position
      cor_let += 1
      check_in_list(guess_list, z, wrongpos_letters)
    else:#Wrong letter
      check_in_list(guess_list, z, wrong_letters)
  return cor_let

#Game Logic
print(Fore.MAGENTA + "\t\t\tWelcome to Wordle!" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "\n\t\tYou have 6 tries to guess a 5 letter word" + Style.RESET_ALL)

#Game Loop
while guess != hidden_word and lives > 0:
  print_words(guessed_words[0], guessed_words[1], guessed_words[2], guessed_words[3], guessed_words[4], guessed_words[5])

  #User Interface
  print(Fore.GREEN + "Correct Letters:" + str(correct_letters))
  print(Fore.RED + "Wrong Letters:" + str(wrong_letters))
  print(Fore.YELLOW + "Wrongly Placed Letters: " + str(wrongpos_letters))
  guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL).upper()

  #Check if the guess length is correct
  while len(guess) > 5 or len(guess) < 5:
    print(Fore.RED + "INVALID INPUT WORD MUST BE 5 LETTERS LONG")
    guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL)
  #Split chars in guess
  for i in guess:
    temp.append(i)
  #Compare chars
  exact_letters = compare_letters(hidden_letters, temp)
  print(temp)
  #Check if the guess is correct
  if guess == hidden_word:
    os.system("clear")
    print(Back.LIGHTGREEN_EX + Fore.BLACK + "You have guess the word correctly!"+ Style.RESET_ALL)
    break
  #Check if some letters are correct
  elif exact_letters > 0:
    os.system("clear")
    print(Fore.YELLOW + "You guessed some of the letters!"+ Style.RESET_ALL)
    guessed_words.insert(counter, guess)
    counter += 1
    lives -= 1
    temp = []
  else:
    os.system("clear")
    print(Back.RED + Fore.BLACK + "Completely incorrect" + Style.RESET_ALL)
    lives -= 1
    guessed_words.insert(counter, guess)
    counter += 1
    for char in guess:
      wrong_letters.append(char)
    temp = []

#Game Over Scenario
if lives <= 0:
  print(Fore.RED + " YOU LOST THE GAME! GO READ SOME DICTIONARY")
  print(Fore.MAGENTA + "The correct word was: " + hidden_word)
else:
  print(Fore.GREEN + " YOU WON THE GAME LIKE YOU SOME KIND OF ENGLISH TEACHER OR SOMETHING")
  