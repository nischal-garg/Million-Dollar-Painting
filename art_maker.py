import turtle as t
from turtle import Turtle, Screen
import random

color_list = [(187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242), (196, 75, 32),
              (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214),
              (210, 152, 96),
              (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50), (218, 130, 155),
              (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111), (162, 29, 27),
              (234, 171, 164), (162, 212, 176), (87, 22, 58), (182, 188, 209), (118, 122, 149), (94, 16, 15)]

print("Welcome to modern art maker!!!")
columns = input("How many columns you want?\n")
rows = input("How many rows you want?\n")

# appearance
turtle = Turtle()
t.colormode(255)
turtle.shape("arrow")
turtle.hideturtle()
turtle.penup()
turtle.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def make_dot():
    # color = random.choice(color_list)
    color = random_color()
    turtle.dot(20, color)


def draw_painting(x, y):
    turtle.setx((-x/2) * 50)
    turtle.sety(-(y/2)*49)

    for _ in range(y):
        turtle.setx((-x/2) * 50)
        turtle.sety(turtle.ycor() + 50)
        for _ in range(x):
            make_dot()
            turtle.fd(50)


draw_painting(int(columns), int(rows))

# screen settings
screen = Screen()
screen.exitonclick()
