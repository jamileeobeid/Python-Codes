Global_1 = "angle"
angle = 50

import turtle

def test_drive():
    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(127)
    turtle.up() 
    turtle.down()
    turtle.goto(50,50)
    turtle.home()
    turtle.circle(25)

def turtle_state():
    print(turtle.isdown() )
    print(turtle.heading() )
    print(turtle.xcor)
    print(turtle.ycor)

def square(x,y,z,angle):
    turtle.begin_fill()
    turtle.left(angle)
    for i in range(4):
       turtle.forward(x)
       turtle.left(90)
    for i in range(4):
       turtle.forward(y)
       turtle.left(90)
    for i in range(4):
       turtle.forward(z)
       turtle.left(90)
    
    turtle.bgcolor("pink")
    turtle.pensize(4)
    turtle.pencolor("red")
    turtle.fillcolor("blue")
    turtle.end_fill()
    turtle.done()
square(200,100,50,angle)