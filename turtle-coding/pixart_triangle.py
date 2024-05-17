import turtle as t

# Declare constants
PIXEL_SIZE = 47
ROWS = 9
COLUMNS = 7

def draw_pixel(x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("plum")
    t.pencolor("magenta")
    t.bgcolor("lightpink")
    t.begin_fill()
    for _ in range(4):
        t.forward(PIXEL_SIZE)
        t.right(90)
    t.end_fill()
    t.penup()

def pixel_art():
    t.speed(0)
    t.pensize(1)
    t.tracer(0)

    for row in range(ROWS):
        for col in range(COLUMNS - row):
            x = col * PIXEL_SIZE - (COLUMNS - row) * PIXEL_SIZE / 2
            y = row * PIXEL_SIZE - (ROWS - 1) * PIXEL_SIZE / 2  # Adjust the y-coordinate
            draw_pixel(x, y)

    t.done()
t.hideturtle()

if __name__ == "__main__":
    pixel_art()
    t.done()