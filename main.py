import random as r
from colorama import Back, Style, Fore
import os
#Possible words to guess

words = []
#Get words from file
with open('words.txt', 'r') as file:
  for line in (line.strip('\n') for line in file):
    up_line = line.upper()
    words.append(up_line)
    
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
ph_word = "_____"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
unused_letters = []

#Functions
def print_words(word1, word2, word3, word4, word5, word6):
  print(Fore.BLUE + "\n\t\t\t\t" + word1 + "\n\t\t\t\t" + word2 + "\n\t\t\t\t" + word3 + "\n\t\t\t\t" + word4 + "\n\t\t\t\t" + word5 + "\n\t\t\t\t" + word6 + "\n")

#Check if the letter is already in list
def check_in_list(list1, counter, list2):
  if list1[counter] in list2:
    pass
  else:
    list2.append(list1[counter])

def check_word(word):
  global words
  while guess in words:
    return True
  else:
    return False
    
def compare_letters(cor_list, guess_list):
  global correct_letters, wrong_letters, wrongpos_letters, ph_word
  cor_let = 0
  for z in range(len(cor_list)):
    if cor_list[z] == guess_list[z]:#Letter at exact position
      replace_letters(guess_list[z])
      cor_let += 1
      check_in_list(guess_list, z, correct_letters)
      #If letter is correct, remove it from wrong position letters
      if guess_list[z] in wrongpos_letters:
        wrongpos_letters.remove(guess_list[z])
    #Correct letter at wrong pos
    elif guess_list[z] in cor_list and guess_list[z] != cor_list[z]:
      #Check if letter is in the word but not at the right position
      cor_let += 1
      check_in_list(guess_list, z, wrongpos_letters)
    else:#Wrong letter
      check_in_list(guess_list, z, wrong_letters)
  return cor_let

#Replace letters in correct word
def replace_letters(letter):
  global hidden_letters, ph_word
  new = ""
  for i in range(len(hidden_letters)):
    if letter == hidden_letters[i]:
      new += letter
    else:
      new += ph_word[i]
  ph_word = new

#Game Logic
print(Fore.MAGENTA + "\t\t\tWelcome to Wordle!" + Style.RESET_ALL)
print(Back.YELLOW + Fore.BLACK + "\n\t\tYou have 6 tries to guess a 5 letter word" + Style.RESET_ALL)

#Game Loop
def gameloop():
  global lives, counter, wrong_letters, wrongpos_letters, correct_letters, temp, ph, guessed_words, guess, ph_word, letters, unused_letters
  
  while guess != hidden_word and lives > 0:
    print_words(guessed_words[0], guessed_words[1], guessed_words[2], guessed_words[3], guessed_words[4], guessed_words[5])
    #Filter available letters
    unused_letters = []
    for i in range(len(letters)):
      if letters[i] in wrong_letters or letters[i] in correct_letters or letters[i] in wrongpos_letters:
        pass
      else:
        unused_letters.append(letters[i])
    #User Interface
    print(Fore.MAGENTA + "The word is: " + ph_word + "\n")
    print(Back.BLACK + Fore.BLUE + "Letters left:\n" + str(unused_letters) + Style.RESET_ALL)
    print(Fore.GREEN + "Correct Letters:" + str(correct_letters))
    print(Fore.RED + "Wrong Letters:" + str(wrong_letters))
    print(Fore.YELLOW + "Wrongly Placed Letters: " + str(wrongpos_letters))
    guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL).upper()
    #Check if the guess length is correct
    while len(guess) > 5 or len(guess) < 5:
      print(Fore.RED + "INVALID INPUT WORD MUST BE 5 LETTERS LONG")
      guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL).upper()
    #Check if the guess is a word
    while guess not in words:
      print(Fore.RED + "INVALID INPUT THE GUESS IS NOT A WORD")
      guess = input(Fore.CYAN + "Enter 5 letter word: " + Style.RESET_ALL).upper()
    #Split chars in guess
    for i in guess:
      temp.append(i)
    #Compare chars
    exact_letters = compare_letters(hidden_letters, temp)
    
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
    input(Fore.YELLOW + "PRESS ENTER TO CONTINUE")
  else:
    print(Back.BLACK + Fore.MAGENTA + "\t\t\t" + ph_word + Style.RESET_ALL)
    print(Fore.GREEN + " YOU WON THE GAME LIKE YOU SOME KIND OF ENGLISH TEACHER OR SOMETHING")
    input(Fore.YELLOW + "PRESS ENTER TO CONTINUE")

  #Restart the game
  choice = input(Back.GREEN + Fore.BLACK + "Type Y to Restart\n" + Back.RED + Fore.BLACK + "Type N to Quit" + Style.RESET_ALL).upper()
  if choice == "Y":
    lives = 6#Number of tries
    counter = 0
    wrong_letters = []
    correct_letters = []#Used letters 
    wrongpos_letters = []
    temp = []
    ph = "*****"
    guessed_words = [ph, ph, ph, ph, ph, ph]
    guess = ""
    ph_word = "_____"
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unused_letters = []
    
    gameloop()
  else: 
    print(Fore.YELLOW + "Thank you for playing!")
    
#Start the game 
gameloop()
    
    