from random import random
import math
from collections import Counter

# I want a program that will populate a "hat" with an arbitrary number of colored balls. Once we have that "hat" filled, we want to be able to pull balls out of it and have the probability for picking a ball of a certain color out of the hat displayed for the user.

# First, we define the number of balls that will fill the container.

number = 0

if number == 0:
    number = int(input("Pick a whole number between 1 and 10: \n"))
    print("You picked: ", number)
else:
    number

# Next, we define the balls that could possibly fill our container.
colored_balls = ["blue", "yellow", "red"]


# Next, we define a method for picking a random ball.
def pick_ball(container):
    index = math.floor(random() * len(container))
    ball = container[index]
    return ball


# Next, we fill our arbitrarily large container with the number of balls that our user picked.
container = []


def fill_container(user_number):
    #     I can use enumerate or count here to keep track of how many items I have in the container.
    for _ in range(user_number):
        container.append(pick_ball(colored_balls))

# I want to calculate the percentage chance of picking a certain color of ball.

# The formula for percentages: (color_ball / total) * 100


fill_container(number)
ball_counter = Counter(container)
print(ball_counter)


def remove_ball(color):
    index = container.index(color)
    removed = container.pop(index)
    ball_counter[color] -= 1
    print(container, removed)


print("blue balls in the ball counter: ", ball_counter["blue"])


def percentage(color):
    percent = round((ball_counter[color] / len(container)) * 100, 2)
    return percent


print("Chance of getting a yellow ball: ", percentage("yellow"))
print("Chance of getting a blue ball: ", percentage("blue"))
print("Chance of getting a red ball: ", percentage("red"))
