import turtle as t

window = t.Screen()
square = t.Turtle()

#Set tracer to False to display image immediatly
t.tracer(False)


"""DEFINE PIXART FUNCTION"""

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


"""PATTERN COLOR FOR MARIO"""

mario_pattern = [
    "00000000000000000000",
    "01111111111111111110",
    "01111112222221111110",
    "01111122222222211110",
    "01111177778781111110",
    "01111787888788811110",
    "01111787788878881110",
    "01111778888777711110",
    "01111118888888111110",
    "01111177277711111110",
    "01111777277277711110",
    "01117777222277771110",
    "01118872822827881110",
    "01118882222228881110",
    "01118822222222881110",
    "01111122211222111110",
    "01111777111177711110",
    "01117777111177771110",
    "01111111111111111110",
    "00000000000000000000"
]

pattern_width = len(mario_pattern[0])
pattern_height = len(mario_pattern)

for i, row in enumerate(mario_pattern):
    for j, color_code in enumerate(row):
        x = (j - pattern_width / 2) * 20
        y = (-i + pattern_height / 2) * 20
        fill_color = "black"  # Default color for 0
        if color_code == "1":
            fill_color = "white"
        elif color_code == "2":
            fill_color = "red"
        elif color_code == "7":
            fill_color = "sienna"
        elif color_code == "8":
            fill_color = "tan"

        #CALL THE PIXART FUNCTION
        draw_square(x, y, fill_color)

# Close the turtle graphics window when clicked
window.exitonclick()