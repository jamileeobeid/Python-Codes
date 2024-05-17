#drawing 5 circles inside of each other using recursion
import turtle as t

def recursive_circles(radius, n):

    #BASE CASE
    if n == 0:
        return None
    
    else:
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.circle(radius)
        t.hideturtle()

        recursive_circles(radius/2, n-1)

recursive_circles(100, 5)
input("press enter to continue") #keeping screen open until user closes it