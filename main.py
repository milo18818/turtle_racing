from turtle import*
from random import randint

print ("place bet on turtel")
bet = input()

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


for turn in range(100):
    red.forward(randint(1, 5))
    blue.forward(randint(1, 5))
    green.forward(randint(1, 5))
    red_pos = red.xcor()
    print("red pos" + str(red_pos))
    blue_pos = blue.xcor()
    print("blue pos" + str(blue_pos))
    green_pos = green.xcor()
    print("green pos" + str(green_pos))

if red_pos > blue_pos:
    print("red win")
elif blue_pos > red_pos:
    print("blue win")
else:
    print("!DRAW!")
