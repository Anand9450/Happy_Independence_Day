import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("white")

# Create the turtle for drawing
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Function to draw the Ashoka Chakra
def draw_chakra(radius, x, y):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color("navy")
    pen.circle(radius)

    # Drawing the 24 spokes
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()

    for _ in range(24):
        pen.forward(radius)
        pen.backward(radius)
        pen.left(15)

# Draw the flag
flag_width = 270
flag_height = 180
stripe_height = flag_height / 3

# Draw the saffron stripe
draw_rectangle("orange", -flag_width / 2, flag_height / 2, flag_width, stripe_height)

# Draw the white stripe
draw_rectangle("white", -flag_width / 2, flag_height / 2 - stripe_height, flag_width, stripe_height)

# Draw the green stripe
draw_rectangle("green", -flag_width / 2, flag_height / 2 - 2 * stripe_height, flag_width, stripe_height)

# Draw the Ashoka Chakra at the center of the white stripe
draw_chakra(stripe_height / 2.5, 0, flag_height / 2 - stripe_height - stripe_height / 2)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()
