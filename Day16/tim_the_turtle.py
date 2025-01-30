from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

tim.shape("turtle")
tim.color("coral")

def tur_triangle():
    tim.forward(100)
    tim.left(120)
    tim.forward(100)
    tim.left(120)
    tim.forward(100)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)

print(my_screen.canvheight)


my_screen.exitonclick()