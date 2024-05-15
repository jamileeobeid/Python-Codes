import turtle as t

""" Drawing the cake """

# Function to draw a rectangle with specified width, height, and color
def draw_rectangle(t, width, height, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

""" Drawing the candles and fire """

# Function to draw a candle
def draw_candle(t, x, y, radius, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.hideturtle()

# Function to draw a fire
def draw_fire(x, y, radius, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.hideturtle()

# Function to draw the middle icing for decorations
def icing(x, y, radius, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.hideturtle()

""" Defining the main function """

# Function to call all other functions
def main():

    '''Asking the user to input parameters for the width of the cake'''

    width = int(input("Enter the width of the cake from -138 to -144: "))
    
    if width > -138:
        print("Sorry, your cake cannot be larger than -138 units wide. Try again!")
    
    elif width < -144:
        print("Sorry, your cake cannot be less than -144 units wide. Try again!")
    
    else:
        print("Your cake is in process! Happiest Birthday!")
        screen = t.Screen()
        screen.bgcolor("mistyrose")
        t.speed(0.3)
        
        # Define rectangle parameters
        rectangles = [
            {"height": 30, "color": "palegreen"},
            {"height": 20, "color": "pink"},
            {"height": 32, "color": "aquamarine"},
            {"height": 20, "color": "plum"}
        ]
        
        # Draw rectangles using the function and parameters
        y_position = 0
        for rect_params in rectangles:
            t.penup()
            t.goto(0, y_position)
            t.pendown()
            draw_rectangle(t, width, rect_params["height"], rect_params["color"])
            y_position += rect_params["height"]
        
        """ Drawing the candles """
        
        # Candle parameters
        x = -70
        y = 101
        radius = 8.5
        color = "magenta"
        
        # Creating another 2 candles
        distance_between_candles = 40
        left_candle = x - distance_between_candles
        right_candle = x + distance_between_candles
        
        # Drawing the candle
        draw_candle(t, x, y, radius, color)
        
        # Drawing the Candles
        draw_candle(t, left_candle, y, radius, color)
        draw_candle(t, right_candle, y, radius, color)
        
        # fire parameters
        x = -70
        y = 114
        radius = 5
        color = "orange"
        
        # Creating 2 other fires
        distance_between_fire = 40
        left_fire = x - distance_between_fire
        right_fire = x + distance_between_fire
        
        # Drawing the middle fires
        draw_fire(x, y, radius, color)
        
        # Drawing side fires
        draw_fire(left_fire, y, radius, color)
        draw_fire(right_fire, y, radius, color)
        
        # fire parameters
        x = -70
        y = 115
        radius = 2.5
        color = "yellow"
        
        # Creating 2 other middle fires
        distance_between_fire = 40
        left_yellowfire = x - distance_between_fire
        right_yellowfire = x + distance_between_fire
        
        # Drawing the middle fires
        draw_fire(x, y, radius, color)
        
        # Drawing side fires
        draw_fire(left_yellowfire, y, radius, color)
        draw_fire(right_yellowfire, y, radius, color)
        
        # Middle icing parameters
        x = -70
        y = 45
        radius = 5
        color = "white"
        
        """ Drawing the icings """

        # Creating multiple middle icings
        distance_between_icings = 10
        one_icing = x - distance_between_icings
        two_icing = x + distance_between_icings
        three_icing = x - 2 * distance_between_icings
        four_icing = x + 2 * distance_between_icings
        five_icing = x - 3 * distance_between_icings
        six_icing = x + 3 * distance_between_icings
        seven_icing = x - 4 * distance_between_icings
        eight_icing = x + 4 * distance_between_icings
        nine_icing = x - 5 * distance_between_icings
        ten_icing = x + 5 * distance_between_icings
        eleven_icing = x - 6 * distance_between_icings
        twelve_icing = x + 6 * distance_between_icings
        thirteen_icing = x - 7 * distance_between_icings
        fourteen_icing = x + 7 * distance_between_icings
        
        # Call the icing function
        icing(x, y, radius, color)
        
        # Drawing the middle icings
        icing(one_icing, y, radius, color)
        icing(two_icing, y, radius, color)
        icing(three_icing, y, radius, color)
        icing(four_icing, y, radius, color)
        icing(five_icing, y, radius, color)
        icing(six_icing, y, radius, color)
        icing(seven_icing, y, radius, color)
        icing(eight_icing, y, radius, color)
        icing(nine_icing, y, radius, color)
        icing(ten_icing, y, radius, color)
        icing(eleven_icing, y, radius, color)
        icing(twelve_icing, y, radius, color)
        icing(thirteen_icing, y, radius, color)
        icing(fourteen_icing, y, radius, color)
        
        # Bottom icing parameters
        x = -70
        y = -2
        radius = 5
        color = "white"
        
        # Creating multiple bottom icings
        distance_between_icings = 10
        zero_icing = x
        one_icing = x - distance_between_icings
        two_icing = x + distance_between_icings
        three_icing = x - 2 * distance_between_icings
        four_icing = x + 2 * distance_between_icings
        five_icing = x - 3 * distance_between_icings
        six_icing = x + 3 * distance_between_icings
        seven_icing = x - 4 * distance_between_icings
        eight_icing = x + 4 * distance_between_icings
        nine_icing = x - 5 * distance_between_icings
        ten_icing = x + 5 * distance_between_icings
        eleven_icing = x - 6 * distance_between_icings
        twelve_icing = x + 6 * distance_between_icings
        thirteen_icing = x - 7 * distance_between_icings
        fourteen_icing = x + 7 * distance_between_icings
        
        # Drawing the bottom icings
        icing(zero_icing, y, radius, color)
        icing(one_icing, y, radius, color)
        icing(two_icing, y, radius, color)
        icing(three_icing, y, radius, color)
        icing(four_icing, y, radius, color)
        icing(five_icing, y, radius, color)
        icing(six_icing, y, radius, color)
        icing(seven_icing, y, radius, color)
        icing(eight_icing, y, radius, color)
        icing(nine_icing, y, radius, color)
        icing(ten_icing, y, radius, color)
        icing(eleven_icing, y, radius, color)
        icing(twelve_icing, y, radius, color)
        icing(thirteen_icing, y, radius, color)
        icing(fourteen_icing, y, radius, color)
        
        # Upper icing parameters
        x = -70
        y = 94.5
        radius = 5
        color = "white"
        
        # Creating multiple Upper icings
        distance_between_icings = 10
        zero_icing = x
        one_icing = x - distance_between_icings
        two_icing = x + distance_between_icings
        three_icing = x - 2 * distance_between_icings
        four_icing = x + 2 * distance_between_icings
        five_icing = x - 3 * distance_between_icings
        six_icing = x + 3 * distance_between_icings
        seven_icing = x - 4 * distance_between_icings
        eight_icing = x + 4 * distance_between_icings
        nine_icing = x - 5 * distance_between_icings
        ten_icing = x + 5 * distance_between_icings
        eleven_icing = x - 6 * distance_between_icings
        twelve_icing = x + 6 * distance_between_icings
        thirteen_icing = x - 7 * distance_between_icings
        fourteen_icing = x + 7 * distance_between_icings
        
        # Call the icing function
        icing(zero_icing, y, radius, color)
        
        # Drawing the upper icings
        icing(one_icing, y, radius, color)
        icing(two_icing, y, radius, color)
        icing(three_icing, y, radius, color)
        icing(four_icing, y, radius, color)
        icing(five_icing, y, radius, color)
        icing(six_icing, y, radius, color)
        icing(seven_icing, y, radius, color)
        icing(eight_icing, y, radius, color)
        icing(nine_icing, y, radius, color)
        icing(ten_icing, y, radius, color)
        icing(eleven_icing, y, radius, color)
        icing(twelve_icing, y, radius, color)
        icing(thirteen_icing, y, radius, color)
        icing(fourteen_icing, y, radius, color)

        """ Prompt the user to enter a color for the table """

        def table_color():
                return input("Enter the desired color of the table: ")
        
        
         # Function for table customization
        def table_customization():
            table_length = input("Enter the length of the table from 270 - 350: ")
            table_length = int(table_length)

        #This if statement restarts the prompt if the user goes against the restrictions.

            if table_length > 350:
                print("Sorry, your table cannot be larger than 350 units. Try again!")
                table_customization()
            elif table_length < 270:
                print("Sorry, your table cannot be less than 270 units. Try again!")
                table_customization()
            else:
                pass
        
            ''' Draw the table '''

            def table_drawing(x, y):
                color = table_color()
                t.pencolor(color)
                t.fillcolor(color)
                t.up()
                t.goto(-60, -41)
                t.begin_fill()
                t.down()
                t.right(180)
                t.forward(x)
                t.right(90)
                t.forward(40)
                t.right(90)
                t.forward(y)
                t.right(90)
                t.forward(40)
                t.right(90)
                t.forward(x)
                t.end_fill()
                
            #   This variable is so that the turtle can draw the table without going off-center, since if the turtle
            #   started from the center and drew off the screen, it wouldn't look presentable. Halving it and then 
            #   having the turtle return to complete the other side makes the table guaranteed to stay centered.

            #   The following function shows that.

            halved_table_length = table_length / 2

            table_drawing(halved_table_length, table_length) 

            """ Draw the table legs """    

            def draw_table_legs():
                    t.goto(71, -41)
                    t.right(270)

                    #Right table leg
                    t.begin_fill()

                    t.forward(225)
                    t.left(270)
                    t.forward(40)
                    t.right(90)
                    t.forward(225)

                    t.end_fill()
                    
                    #Left table leg
                    t.up()
                    t.goto(-190, -41)
                    t.down()

                    t.begin_fill()

                    t.right(180)
                    t.forward(225)
                    t.left(90)
                    t.forward(40)
                    t.left(90)
                    t.forward(225)

                    t.end_fill()
                
                 #Background left table leg 

                 #Using the colour black so that if the user chooses any colour for the table, it looks like its in shadow regardless.
                    t.fillcolor("black")
            
                    t.begin_fill()

                    t.right(90)
                    t.forward(20)
                    t.right(90)
                    t.forward(200)
                    t.right(90)
                    t.forward(20)
                    t.right(90)
                    t.forward(200)
 
                    t.end_fill()

                 #Background right table leg
                    t.up()
                    t.goto(31, -41)

                    t.setheading(270)
 
                    t.fillcolor("black")

                    t.begin_fill()

                    t.forward(200)
                    t.right(90)
                    t.forward(20)
                    t.right(90)
                    t.forward(200)
                    t.right(90)
                    t.forward(20)

                    t.end_fill()
        
            draw_table_legs()

        table_customization()

        # printing the final birthday message
        print("Your birthday cake scene is done! Enjoy your birthday!")
        
        print("Press anywhere on the screen to exit")
        
         # Closing the turtle graphics window when clicked anywhere
        t.exitonclick()
        print("Press anywhere on the screen to exit")

# Calling the main function to run the program
if __name__ == "__main__":
 main()