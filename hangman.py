from random import randint

words = [
  "apple",
  "banana",
  "chair",
  "dog",
  "elephant",
  "friday",
  "giraffe",
  "helicopter",
  "instructions",
  "jolly",
  "knowledge",
  "lemon",
  "mountain"
]

word_index = randint(0, len(words) - 1)
word_choice = words[word_index]
# print(word_choice)

guesses = []
for i in range(len(word_choice)):
  guesses.append("_")
# print(guesses)

chances_left = 10
has_won = False

while chances_left > 0 and has_won == False:
  print(guesses)
  print("Chances Left: " + str(chances_left))
  letter = input("Enter a letter: ")
  is_guess_correct = letter in word_choice
  for i in range(len(word_choice)):
    if (word_choice[i] == letter):
      guesses[i] = letter
  if is_guess_correct == False:
    chances_left = chances_left - 1
    print("Incorrect Guess")
  else:
    print("Correct Guess")
  has_won = not "_" in guesses
  print("")

if has_won == True:
  print("You Won!")
  print("The word was " + word_choice)
else:
  print("You Lost!")
  print("The word was " + word_choice)
