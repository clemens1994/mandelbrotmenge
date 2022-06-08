print("test")
import turtle

shiggy = turtle.Turtle()

# Window
window = turtle.Screen()
window.bgcolor("Black")

# Speed - fast
shiggy.speed(100)

# Square function
def go_full_square():
    for i in range(4):
        shiggy.forward(20)
        shiggy.right(90)

# Yellow Square
def yellow_square():
    shiggy.begin_fill()
    shiggy.color("Yellow")
    go_full_square()
    shiggy.end_fill()
    shiggy.color("Black")

# Green Square
def green_square():
    shiggy.begin_fill()
    shiggy.color("Green")
    go_full_square()
    shiggy.end_fill()
    shiggy.color("Black")

# while True:
#     green_square()
#     shiggy.forward(20)
#     yellow_square()
#     shiggy.forward(20)

# Draw Mandelbrotmenge

# 1.  Determine screen size
window.setup(300,300)
