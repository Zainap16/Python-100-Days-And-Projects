import turtle as t
import random

charlie= t.Turtle()
charlie.speed("fastest")
# draw a circle
t.colormode(255)
# random colors function
def ranColors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    random_colours = (r,g,b)
    return random_colours


def cir(t):
    charlie.tilt(t)

for direction in range(100):
    charlie.color(ranColors())
    cir(direction)
    charlie.circle(100)
    charlie.right(direction)
    
    



# loop many cirles using tilt?



screen = t.Screen()
screen.exitonclick()

# def cir(angle):
#     charlie.circle(100)
#     charlie.right(angle)
#     charlie.circle(100)