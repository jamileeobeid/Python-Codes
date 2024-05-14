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


"""PATTERN COLOR FOR MARIO CHARACTER"""

pattern = [
    "00000000000000000000",
    "09999999999999999990",
    "09999995555559999990",
    "09999555555555999990",
    "09999998080000999990",
    "09999888088808099990",
    "09998880888008099990",
    "09999000088880099990",
    "09999988888889999990",
    "09999999111511999990",
    "09999111511511199990",
    "09991111555511119990",
    "09998815155151889990",
    "09998885555558889990",
    "09998855555555889990",
    "09999955599555999990",
    "09999000999900099990",
    "09990000999900009990",
    "09999999999999999990",
    "00000000000000000000"
]

pattern_width = len(pattern[0])
pattern_height = len(pattern)

for i, row in enumerate(pattern):
    for j, color_code in enumerate(row):
        x = (j - pattern_width / 2) * 20
        y = (-i + pattern_height / 2) * 20
        fill_color = "black"  # Default color for 0
        if color_code == "1":
            fill_color = "white"
        elif color_code == "2":
            fill_color = "tan"
        elif color_code == "3":
            fill_color = "green"
        elif color_code == "5":
            fill_color = "green"
        elif color_code == "8":
            fill_color = "tan"
        elif color_code == "9":
            fill_color = "grey"

        #CALL THE PIXART FUNCTION
        draw_square(x, y, fill_color)

# Close the turtle graphics window when clicked
window.exitonclick()