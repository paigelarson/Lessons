from random import randint

while(True):
    print("Press Enter to roll 2 dice")
    input()
    
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    roll = roll1+roll2
    
    print("You rolled a " + str(roll1)+" and a "+str(roll2)+" for a total of "+str(roll)+"\n")
