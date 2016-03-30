from random import randint

random = randint(0,7)
guess = 0
ram = ""
while ram != random:
    print random
    ram = int(raw_input("make a guess: "))
    if ram < random:
        print "Your guess is less than i need"
    elif ram > random:
            print "your guess is greater than i need"
    guess += 1
else:
    print "Succes with " + str(guess) + " gueses"
