import turtle as t

# Declare constants
PIXEL_SIZE = 50
ROWS = 9
COLUMNS = 7

def draw_pixel(x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Set the pen color to black before drawing the circle
    t.pencolor("magenta")
    t.fillcolor("pink")
    
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def pixel_art():
    t.speed(0)
    t.pensize(1)
    t.tracer(0)

    for row in range(ROWS):
        for col in range(COLUMNS - row):
            x = col * PIXEL_SIZE - (COLUMNS - row) * PIXEL_SIZE / 2
            y = row * PIXEL_SIZE - (ROWS - 1) * PIXEL_SIZE / 2  # Adjust the y-coordinate
            draw_pixel(x, y)

if __name__ == "__main__":
    t.bgcolor("mistyrose")
    pixel_art()
    t.hideturtle()
    t.done()