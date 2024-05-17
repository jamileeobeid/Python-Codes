import turtle as t

#Declaring the constants
PIXEL_SIZE = 20
ROWS = 20
COLUMNS = 20


#Using Test-Driven Development (TDD)
def count_pixels(rows, columns):
    return rows * columns

if __name__ == "__main__":
    def test_count_pixels():
        assert count_pixels(20, 20) == 400
        assert count_pixels(10, 5) == 50
        assert count_pixels(0, 10) == 0 
        assert count_pixels(5, 0) == 0 

    test_count_pixels()



"""DRAWING THE PIXELS"""

def draw_pixel(x, y, color):
    t.speed(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.pencolor("black")
    t.begin_fill()
    for _ in range(4):
        t.forward(PIXEL_SIZE)
        t.right(90)
    t.end_fill()
    t.penup()


def pixel_art():
    t.speed(0)
    t.pensize(0.2)
    t.tracer(0)

    """IMPLEMENTING MATHEMATICAL EQUATIONS TO DRAW THE PIXELS"""
    for row in range(ROWS):
        for col in range(COLUMNS):
            x = col * PIXEL_SIZE - (COLUMNS * PIXEL_SIZE) / 2
            y = (ROWS * PIXEL_SIZE) / 2 - row * PIXEL_SIZE

            # using conditional statements to implement the red and black colors
            if (row + col) % 2 == 0:
                draw_pixel(x, y, "skyblue")
            else:
                draw_pixel(x, y, "midnightblue")

    t.done()

#Calling pixart from the main function
if __name__ == "__main__":
    pixel_art()
    t.done()