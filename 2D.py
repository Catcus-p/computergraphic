from graphics import *

# Create graphics window
win = GraphWin("Window to Viewport Transformation", 800, 600)

# Input window coordinates
xwmin = float(input("Enter xwmin: "))
ywmin = float(input("Enter ywmin: "))
xwmax = float(input("Enter xwmax: "))
ywmax = float(input("Enter ywmax: "))

# Input viewport coordinates
xvmin = float(input("Enter xvmin: "))
yvmin = float(input("Enter yvmin: "))
xvmax = float(input("Enter xvmax: "))
yvmax = float(input("Enter yvmax: "))

# Input triangle coordinates
xw1 = float(input("Enter x1: "))
yw1 = float(input("Enter y1: "))

xw2 = float(input("Enter x2: "))
yw2 = float(input("Enter y2: "))

xw3 = float(input("Enter x3: "))
yw3 = float(input("Enter y3: "))

# Draw window rectangle
window_rect = Rectangle(Point(xwmin, ywmin), Point(xwmax, ywmax))
window_rect.draw(win)

# Draw original triangle
line1 = Line(Point(xw1, yw1), Point(xw2, yw2))
line2 = Line(Point(xw2, yw2), Point(xw3, yw3))
line3 = Line(Point(xw3, yw3), Point(xw1, yw1))

line1.draw(win)
line2.draw(win)
line3.draw(win)

# Window to viewport transformation
xv1 = ((xw1 - xwmin) / (xwmax - xwmin)) * (xvmax - xvmin) + xvmin
yv1 = ((yw1 - ywmin) / (ywmax - ywmin)) * (yvmax - yvmin) + yvmin

xv2 = ((xw2 - xwmin) / (xwmax - xwmin)) * (xvmax - xvmin) + xvmin
yv2 = ((yw2 - ywmin) / (ywmax - ywmin)) * (yvmax - yvmin) + yvmin

xv3 = ((xw3 - xwmin) / (xwmax - xwmin)) * (xvmax - xvmin) + xvmin
yv3 = ((yw3 - ywmin) / (ywmax - ywmin)) * (yvmax - yvmin) + yvmin

# Draw viewport rectangle
viewport_rect = Rectangle(Point(xvmin, yvmin), Point(xvmax, yvmax))
viewport_rect.setOutline("blue")
viewport_rect.draw(win)

# Draw transformed triangle
tline1 = Line(Point(xv1, yv1), Point(xv2, yv2))
tline2 = Line(Point(xv2, yv2), Point(xv3, yv3))
tline3 = Line(Point(xv3, yv3), Point(xv1, yv1))

tline1.setOutline("red")
tline2.setOutline("red")
tline3.setOutline("red")

tline1.draw(win)
tline2.draw(win)
tline3.draw(win)

print("Transformation Completed")

# Wait for mouse click to close
win.getMouse()
win.close()