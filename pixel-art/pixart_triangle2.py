import turtle as t

# Declare constants
PIXEL_SIZE = 54
ROWS = 9
COLUMNS = 7

def draw_pixel(x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("steelblue")
    t.pencolor("midnightblue")
    t.bgcolor("lightcyan")
    t.begin_fill()
    #t.hideturtle()

    for _ in range(3):
        t.forward(PIXEL_SIZE)
        t.left(120)

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