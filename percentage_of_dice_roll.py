from random import randint

def dice_roll():
  roll1 = randint(1, 6)
  roll2 = randint(1, 6)
  return roll1 + roll2

# print(dice_roll())

roll_results = []
for i in range(13):
  roll_results.append(0)

print(roll_results)

trials = 100
for i in range(trials):
  roll = dice_roll()
  roll_results[roll] = roll_results[roll] + 1

print(roll_results)
print("Two dice were rolled 100 times. This is how often each result occured.")

for i in range(len(roll_results)):
  num_rolls = roll_results[i]
  percentage = float(num_rolls) / trials * 100
  print(str(i) + " was rolled " + str(percentage) + "% of the time")
