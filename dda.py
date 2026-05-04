import turtle

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Determine steps
    steps = int(max(abs(dx), abs(dy)))
    if steps == 0:
        steps = 1  # To avoid division by zero

    # Calculate increment
    xinc = dx / steps
    yinc = dy / steps

    x = x1
    y = y1

    # Setup turtle
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Draw line using DDA
    for i in range(steps):
        x += xinc
        y += yinc
        t.goto(round(x), round(y))

    turtle.done()


# Input from user
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

DDA(x1, y1, x2, y2)
       