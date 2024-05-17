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


"""PATTERN COLOR FOR YODA"""

yoda_pattern = [
    "0000000000000000000000000",
    "0111111111111111111111110",
    "0111111111100011111111110",
    "0111111110066600111111110",
    "0111111106656566011111110",
    "0111111096666666901110110",
    "0111000965656565690006010",
    "0110666666666666666665010",
    "0106556555666555666650110",
    "0110005101606101665501110",
    "0111110666666666660011110",
    "0111111066000666601111110",
    "0111111106666666011111110",
    "0111111110066660111111110",
    "0111111100A8778A011111110",
    "011111106AA8778AA01111110",
    "0111110770A8008A601111110",
    "0111111070A8778A011111110",
    "0111111070660066011111110",
    "0111111101001100111111110",
    "0111111111111111111111110",
    "0000000000000000000000000"
]

pattern_width = len(yoda_pattern[0])
pattern_height = len(yoda_pattern)

for i, row in enumerate(yoda_pattern):
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
        elif color_code == "6":
            fill_color = "yellowgreen"
        elif color_code == "7":
            fill_color = "sienna"
        elif color_code == "8":
            fill_color = "tan"
        elif color_code == "9":
            fill_color = "grey"
        elif color_code == "A":
            fill_color = "silver"

        #CALL THE PIXART FUNCTION
        draw_square(x, y, fill_color)

# Close the turtle graphics window when clicked
window.exitonclick()