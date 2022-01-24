import turtle

pen = turtle.Turtle()
pen.speed(0)
colors = ["blue", "green", "orange", "yellow"]

for i in range(100):
    pen.color(colors[i%4])
    pen.circle(5*i)
    pen.right(45)
