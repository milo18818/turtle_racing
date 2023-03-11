from turtle import*
from random import randint
import os


def turtle_race():

    if os.path.isfile("money"):
        f = open("money", "r")
        money = int(f.read())
        f.close()


    print("turtle win?")
    bet = input()

    red_win = 0
    yellow_win = 0
    blue_win = 0
    green_win = 0


    speed(99999999999)
    penup()
    goto(-140, 140)

    for step in range(16):
        write(step, align = "center")
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    red = Turtle()
    red.color("red")
    red.shape("turtle")

    red.penup()
    red.goto(-160, 100)
    red.pendown()

    blue = Turtle()
    blue.color("blue")
    blue.shape("turtle")

    blue.penup()
    blue.goto(-160, 70)
    blue.pendown()

    green = Turtle()
    green.color("green")
    green.shape("turtle")

    green.penup()
    green.goto(-160, 40)
    green.pendown()

    yellow = Turtle()
    yellow.color("yellow")
    yellow.shape("turtle")

    yellow.penup()
    yellow.goto(-160, 10)
    yellow.pendown()


    for turn in range(100):
        red.forward(randint(1, 5))
        blue.forward(randint(1, 5))
        green.forward(randint(1, 5))
        yellow.forward(randint(1,5))
        yellow_pos = yellow.xcor()
        print("yellow pos" + str(yellow_pos))
        red_pos = red.xcor()
        print("red pos" + str(red_pos))
        blue_pos = blue.xcor()
        print("blue pos" + str(blue_pos))
        green_pos = green.xcor()
        print("green pos" + str(green_pos))

    if red_pos > blue_pos and red_pos > green_pos and red_pos > yellow_pos:
        print("red win")
        red_win += 1
    elif blue_pos > red_pos and blue_pos > green_pos and blue_pos > yellow_pos:
        print("blue win")
        blue_win += 1
    elif green_pos > blue_pos and green_pos > red_pos and green_pos > yellow_pos:
        print("green win")
        green_win += 1
    elif yellow_pos > blue_pos and yellow_pos > red_pos and yellow_pos > green_pos:
        print("yellow win")
        yellow_win += 1
    else:
        print("!DRAW!")

    if red_win == 1 and bet == "red":
        print("bet correct (red)")
        money += 100
    elif blue_win == 1 and bet == "blue":
        print("bet correct (blue)")
        money += 100
    elif green_win == 1 and bet == "green":
        print("bet correct (green)")
        money += 100
    elif yellow_win == 1 and bet == "yellow":
        print("bet correct (yellow)")
        money += 100
    else:
        print("bet lost")

    f = open("money", "w")
    f.write(str(money))
    f.close()

    print("money = " + str(money))