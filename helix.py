import turtle

turtle.bgcolor("black")

colors = ["red", "purple", "blue", "green", "orange"]

pen = turtle.Turtle()
pen.speed(0)
for i in range(360):
    pen.color(colors[i%5])
    pen.forward(i)
    pen.left(59)

# create a star using turtle
