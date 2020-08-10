from random import random
import math
from collections import Counter

# I want a program that will populate a "hat" with an arbitrary number of colored balls. Once we have that "hat" filled, we want to be able to pull balls out of it and have the probability for picking a ball of a certain color out of the hat displayed for the user.

# First, we define the number of balls that will fill the container, the player's score, and the last removed item.
number = 0
score = 0
removed = []
results = []

# Next, we declare a container for the balls.
container = []

# Next, we define the balls that could possibly fill our container.
colored_balls = ["blue", "yellow", "red"]

# Next, we define a method for filling the container with balls.


def fill_container(user_number):
    # I can use enumerate or count here to keep track of how many items I have in the container.
    for _ in range(user_number):
        container.append(pick_ball(colored_balls))

# Next, we define a method for picking a random ball.


def pick_ball(container):
    index = math.floor(random() * len(container))
    ball = container[index]
    return ball

# I want to calculate the percentage chance of picking a certain color of ball.


def percentage(color):
    if len(container) == 0:
        return
    percent = round((ball_counter[color] / len(container)) * 100, 2)
    return percent


# I want to use this function to remove a ball at random from the container.
def remove_ball(ball_container, placeholder):
    index = math.floor(random() * len(ball_container))
    placeholder = container.pop(index)
    if len(removed) == 0:
        removed.append(placeholder)
    else:
        removed[0] = placeholder


# Initialization scope: this should run while there are no balls in the container.
while number == 0:
    number = int(input("\nPick a whole number between 1 and 10: \n"))
    print("You picked: ", number)

# Main program scope. This is the loop that will run while there are items inside the container.
while number > 0:

    # fill up the container with balls
    fill_container(number)

    # fill a counter to keep track of the number of items inside the container.
    ball_counter = Counter(container)
    print(ball_counter)

    # set up the main game loop.
    while len(container) > 0:
        next_pick = input(
            "\nWhat color ball are you hoping to get on your next pick?\n(red, yellow, or blue) \n")

        # possible user input error handling.
        if next_pick not in colored_balls:
            next_pick = input(
                "\nOops! Try picking one of the three colors listed here.\n(red, yellow, or blue) \n")

        # handling a correct user pick.
        else:
            print(f'You picked {next_pick}.')

        remove_ball(container, removed)
        number -= 1
        print("Total number of balls left in the hat: ", number)
        print(removed[0])

        # print("\nChance of getting a yellow ball: ", percentage("yellow"))
        # print("\nChance of getting a blue ball: ", percentage("blue"))
        # print("\nChance of getting a red ball: ", percentage("red"))
