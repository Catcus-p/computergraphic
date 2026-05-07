import turtle
import time

# 🟦 Screen Setup
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("white")
screen.title("Midpoint Circle Drawing Algorithm")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()


# 🟨 Draw Coordinate Grid
def draw_grid():
    grid = turtle.Turtle()
    grid.speed(0)
    grid.hideturtle()

    # Grid lines
    grid.color("#dddddd")
    grid.pensize(1)

    for x in range(-400, 401, 25):
        grid.penup()
        grid.goto(x, -400)
        grid.pendown()
        grid.goto(x, 400)

    for y in range(-400, 401, 25):
        grid.penup()
        grid.goto(-400, y)
        grid.pendown()
        grid.goto(400, y)

    # Axes
    grid.color("black")
    grid.pensize(3)

    # X-axis
    grid.penup()
    grid.goto(-400, 0)
    grid.pendown()
    grid.goto(400, 0)

    # Y-axis
    grid.penup()
    grid.goto(0, -400)
    grid.pendown()
    grid.goto(0, 400)

    # Labels
    grid.penup()
    grid.goto(380, 10)
    grid.write("X", font=("Arial", 14, "bold"))

    grid.goto(10, 380)
    grid.write("Y", font=("Arial", 14, "bold"))

    # Origin
    grid.goto(5, 5)
    grid.write("(0,0)", font=("Arial", 10, "bold"))


# 🟥 Plot Pixel
def put_pixel(x, y):
    pen.goto(x, y)
    pen.dot(5, "blue")


# 🟢 Midpoint Circle Algorithm
def draw_circle(h, k, r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:

        # 8 symmetric points
        put_pixel(x + h, y + k)
        put_pixel(-x + h, y + k)
        put_pixel(x + h, -y + k)
        put_pixel(-x + h, -y + k)

        put_pixel(y + h, x + k)
        put_pixel(-y + h, x + k)
        put_pixel(y + h, -x + k)
        put_pixel(-y + h, -x + k)

        time.sleep(0.03)

        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1

    # Show only important points
    pen.goto(h + r + 10, k)
    pen.write(f"Radius = {r}", font=("Arial", 10, "bold"))

    pen.goto(h + 10, k + 10)
    pen.write(f"Center({h},{k})", font=("Arial", 10, "bold"))


# 🟣 Draw Grid
draw_grid()

# 🟢 Input
h = int(input("Enter center h: "))
k = int(input("Enter center k: "))
r = int(input("Enter radius: "))

# Draw center point
pen.goto(h, k)
pen.dot(8, "red")

# Draw circle
draw_circle(h, k, r)

turtle.done()