import random
from turtle import Turtle, Screen

tim = Turtle()

tim.width(15) 

# go in random directions
directions = [1,90,180,270]
# angle = 360 / counter

c = ['blue', 'red', 'green','salmon1','coral','SkyBlue','OrangeRed']
tim.speed("fastest")
tim.shape("turtle")
for _ in range(100):
    # counter = random.randrange(1,360,45)
    steps = 30
    tim.forward(steps)
    # tim.right(90)
    tim.setheading(random.choice(directions))
    ac = random.choice(c)
    tim.color(ac)
    

screen = Screen()
screen.exitonclick()
