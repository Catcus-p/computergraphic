import turtle

#  Draw Coordinate Grid
def draw_grid():
    screen = turtle.Screen()
    screen.setup(900, 900)
    screen.bgcolor("white")
    screen.title("Bresenham Line Drawing with Coordinate System")

    grid = turtle.Turtle()
    grid.speed(0)
    grid.hideturtle()

    # Light grid lines
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

    # Labels
    grid.penup()
    grid.goto(380, 10)
    grid.write("X", font=("Arial", 14, "bold"))

    grid.goto(10, 380)
    grid.write("Y", font=("Arial", 14, "bold"))

    # Origin
    grid.goto(5, 5)
    grid.write("(0,0)", font=("Arial", 10, "bold"))


#  Bresenham Algorithm (Clean)
def bresenham(x1, y1, x2, y2):
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()

    # Convert to integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    # Save start and end
    start_x, start_y = x1, y1
    end_x, end_y = x2, y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    while True:
        # Draw point
        t.goto(x1, y1)
        t.dot(5, "blue")

        # Show only start point
        if x1 == start_x and y1 == start_y:
            t.goto(x1 + 10, y1 + 10)
            t.write(f"Start({x1},{y1})", font=("Arial", 10, "bold"))

        # Show only end point
        if x1 == end_x and y1 == end_y:
            t.goto(x1 + 10, y1 + 10)
            t.write(f"End({x1},{y1})", font=("Arial", 10, "bold"))

        # Stop condition
        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy



draw_grid()

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

bresenham(x1, y1, x2, y2)

turtle.done()