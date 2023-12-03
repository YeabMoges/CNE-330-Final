import turtle
import time

def center(trt):
    trt.hideturtle()
    trt.penup()
    trt.goto(0,200)
    trt.left(90)
    trt.pendown()

def drawCircle():
    c.hideturtle()
    c.circle(200)
    c.penup()
    # c.write("VI",align="center", font=("serif", 25, "normal"))
    # c.left(90)
    # c.forward(367)
    # c.write("XII", align="center", font=("serif", 25, "normal"))
    # c.right(180)
    # c.forward(167)
    # c.right(90)
    # c.forward(193)
    # c.write("IX", align="left", font=("serif", 25, "normal"))
    # c.right(180)
    # c.forward(393)
    # c.write("III", align="right", font=("serif", 25, "normal"))
    time_in_roman = ['VI', 'III', 'XII', 'IX']
    c.right(45)
    for i in range(4):
        c.write(time_in_roman[i], align="center", font=("serif", 25, "normal"))
        c.left(90)
        c.forward(255)





def hour(a):
    h.hideturtle()
    h.setheading(a)
    h.forward(70)


def minute(a):
    m.hideturtle()
    m.setheading(a)
    m.forward(135)

def second(a):
    s.pencolor("red")
    s.hideturtle()
    s.setheading(a)
    s.forward(170)

c = turtle.Turtle()        # create alex
h = turtle.Turtle()
m = turtle.Turtle()
s = turtle.Turtle()
c.pensize(6)
h.pensize(5)
m.pensize(4)
s.pensize(3)
drawCircle()

center(h)
center(m)
center(s)

while True:
    # Get the current time
    current_time = time.localtime()
    hr = current_time.tm_hour % 12  # 12-hour format
    mn = current_time.tm_min
    sc = current_time.tm_sec

    # Calculate angles for hour, minute, and second hands
    h_angle = -(hr * 30 + mn / 2)  # 30 degrees per hour, 0.5 degrees per minute
    m_angle = -mn * 6  # 6 degrees per minute
    s_angle = -sc * 6  # 6 degrees per second

    h.clear(),m.clear(),s.clear()  # Clear previous drawings
    hour(90+h_angle)  # Draw the hour hand
    center(h)
    minute(90+m_angle)  # Draw the minute hand
    center(m)
    second(90+s_angle)  # Draw the second hand
    center(s)

    turtle.update()  # Update the display
    time.sleep(1)  # Wait for one second


wn = turtle.Screen()          # Set up the window and its attributes




wn.exitonclick()