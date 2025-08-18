import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Harry Potter Glasses")

pen = turtle.Turtle()
pen.pensize(3)

# Left glass
pen.penup()
pen.goto(-60, 0)
pen.pendown()
pen.circle(50)

# Right glass
pen.penup()
pen.goto(60, 0)
pen.pendown()
pen.circle(50)

# Bridge between glasses
pen.penup()
pen.goto(-10, 50)
pen.pendown()
pen.forward(20)

turtle.done()
