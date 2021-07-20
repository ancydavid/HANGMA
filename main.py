

import random
import hangman_arts
import hangman_words

print(hangman_arts.logo)

n= len(hangman_arts.stages) -1
#print(stages[n])
lives = 6
#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.

display = []
insert1 = []

for letter in chosen_word:
  display.append('-')
#print(display) 

#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
end_of_game = False 
while not end_of_game: 
  guess = input("Guess a letter: ").lower()
  if guess not in insert1:
      insert1.append(guess)
      #print(insert1)
  else:
    print("Letter already entered")
  for position in range(0, len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:

            display[position] = letter
            #print(display)
        
          
      if "-" not in display:
        print("you won")
        end_of_game = True 
  #If guess is not a letter in the chosen_word,
      #Then reduce 'lives' by 1. 
      #If lives goes down to 0 then the game should stop and it should print "You lose."      
  if guess not in chosen_word:
      print(hangman_arts.stages[n])
      print("YOU HAVE CHOSEN WRONG LETTER AND YOU LOSE A LIFE")
      n= n-1;
  if n == 0:
    print("YOU LOSE")
    end_of_game = True    
  

      #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

      