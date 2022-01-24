import turtle
sides = int(input("Enter number of sides: "))
window = turtle.Screen()
window.bgcolor("light green")
window.title("Turtle")
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.speed(0)
# regular figure


for i in range(sides):
    pen.forward(100)
    pen.right(360//sides)

