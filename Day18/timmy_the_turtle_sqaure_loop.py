# draw a square with turtle garphos
from turtle import Turtle, Screen
import random
timmy = Turtle()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)
counter = 4


# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
c = ['blue', 'red', 'green','salmon1','coral','SkyBlue','OrangeRed']
timmy.shape("turtle")
timmy.width(5)
for stop in range(counter):
    temp = (360 / counter)
    ac = random.choice(c)
    for _ in range(counter):
        timmy.color(ac)
        timmy.forward(100)
        timmy.right(temp)
    counter +=1
    
    
    

print(timmy.pos())


screen = Screen()
screen.exitonclick()