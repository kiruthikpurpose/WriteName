import turtle

# Step 1: Import Libraries
import turtle
import string

# Step 2: Set Up the Turtle Screen
screen = turtle.Screen()
screen.title("Draw Your Name with Turtle")
screen.bgcolor("white")

# Initialize the turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# Step 3: Define Functions to Draw Each Letter
def draw_a(pen):
    pen.setheading(60)
    pen.forward(50)
    pen.right(120)
    pen.forward(50)
    pen.backward(25)
    pen.right(120)
    pen.forward(25)
    pen.backward(25)
    pen.left(120)
    pen.forward(25)
    pen.right(60)

def draw_b(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(90)
    pen.circle(-12.5, 180)
    pen.right(180)
    pen.circle(-12.5, 180)
    pen.penup()
    pen.right(90)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_c(pen):
    pen.setheading(0)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.backward(25)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(25)
    pen.penup()
    pen.backward(25)
    pen.left(90)
    pen.backward(50)
    pen.left(90)
    pen.pendown()

def draw_d(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(90)
    pen.circle(-25, 180)
    pen.right(90)
    pen.penup()
    pen.forward(50)
    pen.right(90)
    pen.pendown()

def draw_e(pen):
    pen.setheading(0)
    pen.forward(25)
    pen.backward(25)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(20)
    pen.backward(20)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.penup()
    pen.backward(25)
    pen.left(90)
    pen.forward(50)
    pen.right(90)
    pen.pendown()

def draw_f(pen):
    pen.setheading(0)
    pen.forward(25)
    pen.backward(25)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(20)
    pen.backward(20)
    pen.right(90)
    pen.forward(25)
    pen.penup()
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_g(pen):
    pen.setheading(0)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.backward(25)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(15)
    pen.penup()
    pen.backward(15)
    pen.right(90)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_h(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(25)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.backward(50)
    pen.left(90)
    pen.penup()
    pen.forward(50)
    pen.right(90)
    pen.pendown()

def draw_i(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(25)
    pen.right(90)
    pen.penup()
    pen.forward(12.5)
    pen.right(90)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_j(pen):
    pen.setheading(0)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.backward(25)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(10)
    pen.penup()
    pen.backward(10)
    pen.right(90)
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_k(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(25)
    pen.right(45)
    pen.forward(35)
    pen.backward(35)
    pen.right(90)
    pen.forward(35)
    pen.backward(35)
    pen.left(135)
    pen.penup()
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_l(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(50)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.penup()
    pen.forward(50)
    pen.right(90)
    pen.pendown()

def draw_m(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(135)
    pen.forward(35)
    pen.left(90)
    pen.forward(35)
    pen.right(135)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_n(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(135)
    pen.forward(70)
    pen.left(135)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_o(pen):
    pen.setheading(0)
    pen.circle(25)
    pen.penup()
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.pendown()

def draw_p(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(90)
    pen.circle(-12.5, 180)
    pen.right(90)
    pen.penup()
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_q(pen):
    pen.setheading(0)
    pen.circle(25)
    pen.setheading(45)
    pen.forward(15)
    pen.backward(30)
    pen.penup()
    pen.forward(15)
    pen.right(135)
    pen.forward(50)
    pen.left(90)
    pen.pendown()

def draw_r(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.right(90)
    pen.circle(-12.5, 180)
    pen.right(90)
    pen.forward(25)
    pen.left(135)
    pen.forward(35)
    pen.backward(35)
    pen.left(45)
    pen.penup()
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_s(pen):
    pen.setheading(0)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.backward(25)
    pen.right(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.forward(25)
    pen.right(90)
    pen.forward(25)
    pen.right(90)
    pen.forward(25)
    pen.penup()
    pen.backward(25)
    pen.left(90)
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_t(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(50)
    pen.right(90)
    pen.forward(25)
    pen.penup()
    pen.backward(12.5)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.pendown()

def draw_u(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(50)
    pen.right(90)
    pen.forward(25)
    pen.right(90)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.left(90)
    pen.forward(25)
    pen.left(90)
    pen.pendown()

def draw_v(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(50)
    pen.right(45)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(135)
    pen.penup()
    pen.forward(50)
    pen.right(90)
    pen.pendown()

def draw_w(pen):
    pen.setheading(90)
    pen.forward(50)
    pen.backward(50)
    pen.right(45)
    pen.forward(35)
    pen.left(90)
    pen.forward(35)
    pen.right(135)
    pen.forward(50)
    pen.penup()
    pen.backward(50)
    pen.right(90)
    pen.pendown()

def draw_x(pen):
    pen.setheading(45)
    pen.forward(50)
    pen.backward(25)
    pen.right(90)
    pen.forward(25)
    pen.backward(50)
    pen.penup()
    pen.forward(25)
    pen.left(45)
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_y(pen):
    pen.setheading(90)
    pen.forward(25)
    pen.right(45)
    pen.forward(35)
    pen.backward(35)
    pen.right(90)
    pen.forward(35)
    pen.backward(35)
    pen.left(45)
    pen.penup()
    pen.forward(25)
    pen.right(90)
    pen.pendown()

def draw_z(pen):
    pen.setheading(0)
    pen.forward(25)
    pen.right(135)
    pen.forward(35)
    pen.left(135)
    pen.forward(25)
    pen.penup()
    pen.backward(25)
    pen.right(90)
    pen.forward(50)
    pen.left(90)
    pen.pendown()

def draw_letter(pen, letter):
    if letter == 'A':
        draw_a(pen)
    elif letter == 'B':
        draw_b(pen)
    elif letter == 'C':
        draw_c(pen)
    elif letter == 'D':
        draw_d(pen)
    elif letter == 'E':
        draw_e(pen)
    elif letter == 'F':
        draw_f(pen)
    elif letter == 'G':
        draw_g(pen)
    elif letter == 'H':
        draw_h(pen)
    elif letter == 'I':
        draw_i(pen)
    elif letter == 'J':
        draw_j(pen)
    elif letter == 'K':
        draw_k(pen)
    elif letter == 'L':
        draw_l(pen)
    elif letter == 'M':
        draw_m(pen)
    elif letter == 'N':
        draw_n(pen)
    elif letter == 'O':
        draw_o(pen)
    elif letter == 'P':
        draw_p(pen)
    elif letter == 'Q':
        draw_q(pen)
    elif letter == 'R':
        draw_r(pen)
    elif letter == 'S':
        draw_s(pen)
    elif letter == 'T':
        draw_t(pen)
    elif letter == 'U':
        draw_u(pen)
    elif letter == 'V':
        draw_v(pen)
    elif letter == 'W':
        draw_w(pen)
    elif letter == 'X':
        draw_x(pen)
    elif letter == 'Y':
        draw_y(pen)
    elif letter == 'Z':
        draw_z(pen)
    pen.penup()
    pen.forward(50)  # Adjust the spacing between letters
    pen.pendown()

# Step 4: Get User Input
user_name = screen.textinput("Name Input", "Enter your name: ").upper()

# Step 5: Draw the Name
pen.penup()
pen.goto(-200, 0)
pen.pendown()

for letter in user_name:
    if letter in string.ascii_uppercase:
        draw_letter(pen, letter)

# Hide the turtle and finish
pen.hideturtle()
screen.mainloop()