import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.title("Midpoint Circle Drawing Algorithm")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()

def put_pixel(x, y):
    pen.goto(x, y)
    pen.dot(4)  # draw a small dot

def draw_circle(h, k, r):
    x = 0
    y = r
    p = 1 - r  # Initial decision parameter

    while x <= y:
        # Plot all 8 symmetric points
        put_pixel(x + h, y + k)
        put_pixel(-x + h, y + k)
        put_pixel(x + h, -y + k)
        put_pixel(-x + h, -y + k)

        put_pixel(y + h, x + k)
        put_pixel(-y + h, x + k)
        put_pixel(y + h, -x + k)
        put_pixel(-y + h, -x + k)

        time.sleep(0.05)  # delay like delay(100)

        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1


# Input from user
h = int(input("Enter center h: "))
k = int(input("Enter center k: "))
r = int(input("Enter radius: "))

draw_circle(h, k, r)

turtle.done()