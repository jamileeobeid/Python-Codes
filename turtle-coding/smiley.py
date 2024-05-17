# Here are the co-ordinates that must me input:
# Enter the x-coordinate: 50
# Enter the y-coordinate: 75
# Enter the x-coordinate: -50
# Enter the y-coordinate: 75

import turtle as t

#Drawing the face
def draw_centered_circle():
    t.color("yellow")
    #black outline the circle
    t.pencolor('black')
    #color fill the circle
    t.fillcolor('yellow')
    t.penup()
    t.goto(-5,-10)
    t.pendown()
    t.begin_fill()
    #draw a circle of a given radius
    t.circle(90)
    #end the filling 
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(75)
    t.right(90)
    t.pendown()

# Drawing the nose
def draw_smiley():
    t.setheading(0)
    t.pencolor('black')
    t.begin_fill()
    t.penup()
    t.circle(12)
    t.fillcolor('pink') 
    t.end_fill()
    #t.hideturtle

# 
def tweak():
    t.speed(1)
    t.tracer(False)
    t.hideturtle()

def draw_eye(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#Drawing the eye
#Starting with the white part
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('white')
    #draw a circle of a given radius
    t.circle(25)
    #end the filling 
    t.end_fill()

#Drawing the iris
def draw_iris(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#start filling in 
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('brown')
    #draw a circle of a given radius
    t.circle(12.5)
    #end the filling 
    t.end_fill()

#Drawintg the pupil
def draw_pupil(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#start filling in 
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('black')
    #draw a circle of a given radius
    t.circle(6.25)
    #end the filling 
    t.end_fill()

#Drawing the right eye
def draw_righteye(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#start filling in 
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('white')
    #draw a circle of a given radius
    t.circle(25)
    #end the filling 
    t.end_fill()

def draw_rightiris(x,y):
#start filling in 
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('brown')
    #draw a circle of a given radius
    t.circle(12.5)
    #end the filling 
    t.end_fill()

def draw_rightpupil(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#start filling in 
    t.begin_fill()
    #fill in the circle with color
    t.fillcolor('black')
    #draw a circle of a given radius
    t.circle(6.25)
    #end the filling 
    t.end_fill()

def draw_mouth(r, y, arc, color):
    t.penup()
    t.goto(35, 50 -r)
    t.setheading(90)
    t.fillcolor(color)
    t.forward(r)
    t.begin_fill()
    t.circle(r, arc)
    t.end_fill()

def main():
    x1= int(input('Enter the x-coordinate: '))
    y1= int(input('Enter the y-coordinate: '))
    x2= int(input('Enter the x-coordinate: '))
    y2= int(input('Enter the y-coordinate: '))

    tweak()
    draw_centered_circle()
    draw_smiley()
    draw_eye(x1,y1)
    draw_iris(x1,y1)
    draw_pupil(x1,y1)
    draw_righteye(x2,y2)
    draw_rightiris(x2,y2)
    draw_rightpupil(x2,y2)
    draw_mouth(40, 60 ,-180, 'black')
    t.hideturtle()
    input("Press to continue")
main()