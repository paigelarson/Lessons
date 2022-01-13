from random import randint
run=True
while(run):
    print("Press Enter to Flip a Coin")
    input()
    coin_flip = randint(1, 2)
    if coin_flip == 1:
        print("heads")
    else:
        print("tails")


