import turtle


def draw_grid():
    screen = turtle.Screen()
    screen.setup(900, 900)
    screen.bgcolor("white")
    screen.title("DDA Line Drawing on Coordinate Graph")

    grid = turtle.Turtle()
    grid.speed(0)
    grid.hideturtle()

    # Small grid lines
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

    # Main axes
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

    # Arrow for X-axis
    grid.penup()
    grid.goto(400, 0)
    grid.setheading(0)
    grid.stamp()

    # Arrow for Y-axis
    grid.goto(0, 400)
    grid.setheading(90)
    grid.stamp()

    # Numbers on X-axis
    grid.color("blue")
    for x in range(-400, 401, 50):
        if x != 0:
            grid.penup()
            grid.goto(x, -18)
            grid.write(str(x), align="center", font=("Arial", 8, "normal"))

    # Numbers on Y-axis
    for y in range(-400, 401, 50):
        if y != 0:
            grid.penup()
            grid.goto(10, y - 5)
            grid.write(str(y), font=("Arial", 8, "normal"))

    # Origin label
    grid.color("red")
    grid.penup()
    grid.goto(5, 5)
    grid.write("(0,0)", font=("Arial", 10, "bold"))

    # Axis labels
    grid.color("black")
    grid.goto(380, 15)
    grid.write("X", font=("Arial", 14, "bold"))

    grid.goto(15, 380)
    grid.write("Y", font=("Arial", 14, "bold"))


def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))
    if steps == 0:
        steps = 1

    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.pensize(4)
    t.penup()
    t.goto(x, y)
    t.dot(8, "green")  # starting point
    t.pendown()

    for i in range(steps):
        x += xinc
        y += yinc
        t.goto(round(x), round(y))

    t.dot(8, "purple")  # ending point


draw_grid()

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

DDA(x1, y1, x2, y2)

turtle.done()