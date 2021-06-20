import random
def game():
    print("Now,Choose a color from the above list:")
    choosen=input()
    if choosen not in color:
        print("You have not choosed from the above list")
        game()
    else:
        pass
    random_choice=(random.choice(color))
    print(random_choice)
    if random_choice==choosen:
        print("Hurray! You Won the Game")
        exit()
    else:
        print("Ohh Noo..You failed to guess...!")
color=['Violet','Indigo','Blue','Green','Yellow','Orange','Red']
print(color)
game()
print("You have two more Chances to guess..")
game()
print("You have one more Chance to guess..")
game()
print("You lost the Game")









