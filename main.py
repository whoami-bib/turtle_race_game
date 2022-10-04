import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=500)
is_race_on=False
user_input=screen.textinput(title="Make Your Bet",prompt="Which turtle will will?choose a color:")
colors=["red", "orange", "yellow", "green", "blue"]
y_positions=[-100,-50,0,50,100]
all_turtles=[]
for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-230, y_positions[i])
    all_turtles.append(tim)
if user_input:
    is_race_on=True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor()>230:
            winning_color=turtles.color()
            if winning_color == user_input.lower():
                print('You Have won.')
            else:
                print(f"Sorry boss you have lost! The winning color is {winning_color}")
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtles.forward(random_distance)




screen.exitonclick()
