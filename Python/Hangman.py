import random

wordlist = ["apple", "orange", "shoe", "hangman", "python"]
hangmanGraphic = ["""
   ====+
   |   |
       |
       |
       |
       |
 ======+
""", """
   ====+
   |   |
   O   |
       |
       |
       |
 ======+
""", """
   ====+
   |   |
   O   |
   |   |
       |
       |
 ======+
""", """
   ====+
   |   |
   O   |
  /|   |
       |
       |
 ======+
""", """
   ====+
   |   |
   O   |
  /|\\  |
       |
       |
 ======+
""", """
   ====+
   |   |
   O   |
  /|\\  |
  /    |
       |
 ======+
""", """
   ====+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
 ======+
""", ]

def hangman(words, hangman):
   
   answerWord = random.choice(words)
   hangmanState = 0
   displayWord = ""
   guessedLetters = []

   for x in answerWord:
      displayWord += "-"

   print(hangman[hangmanState])
   print(f"Guess the word. It has {len(answerWord)} letters.")
   print(displayWord)

   while True:
      if answerWord == displayWord:
         print(f"You win. The word was {answerWord}.")
         break

      elif hangmanState == 6:
         print(f"You lose. The word was {answerWord}.")
         break

      else:
         guess = input()
         
         displayWord = ""

         if guess in answerWord:
            guessedLetters.append(guess)

            for x in answerWord:
               if x in guessedLetters:
                  displayWord += x

               else:
                  displayWord += "-"

         else:
            hangmanState += 1
            for x in answerWord:
               if x in guessedLetters:
                  displayWord += x

               else:
                  displayWord += "-"

      print(hangman[hangmanState])
      print(displayWord)



hangman(wordlist, hangmanGraphic)
input()

# Thanks DancingElbow#3534