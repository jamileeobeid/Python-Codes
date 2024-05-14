import turtle as t

# Declare constants
PIXEL_SIZE = 20
ROWS = 30
COLUMNS = 30

def draw_pixel(x, y):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("darkviolet")
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
        for col in range(COLUMNS):
            x = col * PIXEL_SIZE - (COLUMNS * PIXEL_SIZE) / 2
            y = (ROWS * PIXEL_SIZE) / 2 - row * PIXEL_SIZE
            draw_pixel(x, y)

    t.done()

if __name__ == "__main__":
    pixel_art()
    t.done()