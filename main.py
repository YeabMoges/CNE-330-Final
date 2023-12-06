# CNE330, Fall 2023
# Yeabsira Moges
# Turtle Wall Clock

import turtle, time

# Positioning the turtles to center
def center(trt):
    trt.hideturtle()
    trt.penup()
    trt.goto(0,200)
    trt.left(90)
    trt.pendown()

# Draw the clock nad its attributes
def drawCircle():
    c.speed(100)
    cc.speed(100)
    dot.speed(100)
    c.begin_fill()
    cc.begin_fill()
    c.hideturtle()
    cc.hideturtle()
    dot.penup()
    dot.hideturtle()
    cc.left(90)
    cc.penup()
    cc.forward(40)
    cc.pendown()
    cc.right(90)
    cc.circle(160)
    c.circle(200)
    c.penup()

    #Build Clock Numbers
    time_in_roman = ['VI', 'III', 'XII', 'IX']
    c.right(45)
    for i in range(4):
        c.write(time_in_roman[i], align="center", font=("Times New Roman", 25, "normal"))
        c.left(90)
        c.forward(255)
    cc.end_fill()
    c.end_fill()

    #Build Dot for Numbers
    dot.right(14)
    for i in range(13):
        if i % 3 != 0:
            dot.write(".", font=("serif", 35, "normal"))
        else:
            dot.write("")
        dot.left(30)
        dot.forward(98)
    dot.pendown()

    #Build Center Dot
    turtle.penup()
    turtle.goto(0, 200)
    turtle.dot(20, "black")

    #Build Numerical Houring
    box.speed(100)
    box.hideturtle()
    box.penup()
    box.goto(20,262)
    box.pendown()
    box.begin_fill()
    for i in range(2):
        box.forward(80)
        box.left(90)
        box.forward(35)
        box.left(90)
    box.end_fill()

    num.speed(100)
    num.penup()
    num.goto(60, 260)
    num.pendown()
    num.hideturtle()

# Set Hour Arm
def hour(a):
    h.speed(1000)
    h.setheading(a)
    h.right(180)
    h.forward(30)
    h.left(180)
    h.forward(120)


# Set Minute Arm
def minute(a):
    m.speed(1000)
    m.setheading(a)
    m.right(180)
    m.forward(30)
    m.left(180)
    m.forward(165)


# Set the Second Arm
def second(a):
    s.pencolor("red")
    s.speed(1000)
    s.setheading(a)
    s.right(180)
    s.forward(30)
    s.left(180)
    s.forward(200)




c = turtle.Turtle()                     # c is for the circle turtle
cc = turtle.Turtle()
h = turtle.Turtle()                     # h is for the hour clock turtle
m = turtle.Turtle()                     # m is for the minute clock turtle
s = turtle.Turtle()                     # s is for the second clock turtle
dot = turtle.Turtle()                   # dot is for number indicators
box = turtle.Turtle()
num = turtle.Turtle()




box.fillcolor("lightgrey")
c.pensize(6)
cc.pensize(5)
c.fillcolor("silver")
cc.fillcolor("grey")

dot.pensize(1), dot.pencolor("red")
h.pensize(6), m.pensize(4), s.pensize(3)

drawCircle()
center(h), center(m), center(s)

while True:

    # Get the current time
    current_time = time.localtime()
    hr = current_time.tm_hour % 12
    mn = current_time.tm_min
    sc = current_time.tm_sec

    # Double digitalize the hour and minute
    def doubleDgt(number):
        if number <= 10:
            self = str(number)
            return ("0" + self)
        else:
            return str(number)

    num.clear()
    num.write(f"{doubleDgt(hr)}:{doubleDgt(mn)}",align="center", font=("Times New Roman", 25, "normal"))


    # Calculate angles for hour, minute, and second hands
    h_angle = -(hr * 30 + mn / 2)
    m_angle = -mn * 6
    s_angle = -sc * 6

    h.clear(),m.clear(),s.clear()  # Clear previous drawings
    hour(90+h_angle)
    center(h)
    minute(90+m_angle)
    center(m)
    second(90+s_angle)
    center(s)

    time.sleep(1)  # Wait for one second

wn = turtle.Screen()          # Set up the window and its attributes
wn.exitonclick()