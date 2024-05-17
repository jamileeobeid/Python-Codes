import turtle as t

window = t.Screen()
square = t.Turtle()

#Set tracer to False to display image immediatly
t.tracer(False)


"""DEFINE THE PIXART FUNCTION"""

def draw_square(x, y, fill_color):
    square.penup()
    square.fillcolor(fill_color)
    square.goto(x, y)
    square.pendown()
    square.begin_fill()
    for _ in range(4):
        square.forward(20)
        square.right(90)
    square.end_fill()


"""PATTERN COLOR FOR STAR"""

star_pattern = [
    "00000000000000000000",
    "01111111111111111110",
    "01111111111111111110",
    "01111111100111111110",
    "01111111033011111110",
    "01111110333301111110",
    "01000000333300000010",
    "01033333333333333010",
    "01104333033033340110",
    "01110433033033401110",
    "01111043033034011110",
    "01111043333334011110",
    "01110433333333401110",
    "01110433333333401110",
    "01104334400443340110",
    "01104440011004440110",
    "01044001111110044010",
    "01000111111111100010",
    "01111111111111111110",
    "00000000000000000000"
]

pattern_width = len(star_pattern[0])
pattern_height = len(star_pattern)

for i, row in enumerate(star_pattern):
    for j, color_code in enumerate(row):
        x = (j - pattern_width / 2) * 20
        y = (-i + pattern_height / 2) * 20
        fill_color = "black"  # Default color for 0
        if color_code == "1":
            fill_color = "white"
        elif color_code == "2":
            fill_color = "tan"
        elif color_code == "3":
            fill_color = "yellow"
        elif color_code == "4":
            fill_color = "orange"

        #CALL THE PIXART FUNCTION
        draw_square(x, y, fill_color)

# Close the turtle graphics window when clicked
window.exitonclick()
