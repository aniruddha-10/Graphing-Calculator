# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: Zack Hassan
# ID: 30152762
# Date: 22/10/2021
# Description: Constructing a Graphing Calculator In Python using math,turle library and Functions.Each functions having their own functionality and perform tasks accrodinly like drawing axes and ticks and expressions(curves)

from math import *
import turtle

#Constants
BACKGROUND_COLOR = "white"    # colour declared as constant for making the background white
WIDTH = 800                   # Width of the turtle window screen specified as a constant
HEIGHT = 600                  # Height of the turtle window screen specified as a constant
AXIS_COLOR = "black"          # Colour declared as constant for making the axis colour as Black
delta = 0.1                   # delta variable declared for making the curves smooth
spacing = 1                   # spacing variable declared so as to maintain each of the spaces between the ticks
adjustment_value_for_tick = 5
adjustment_value_for_labels = 20

#FUNCTIONS FOR THE PROGRAM

#FUNCTION FOR THE COLOURS OF THE CURVES TO BE DRAWN ON THE SCREEN
def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    if(equation_counter%3 == 0):       # checks the condition if the remainder division gives out 0 or not so that the function will return the string of the colour name
        return "red"
    elif(equation_counter%3 == 1):     # checks the condition if the remainder division gives out 1 or not so that the function will return the string of the colour naem
        return "green"
    elif(equation_counter%3 == 2):     # checks the condition if the remainder division gives out 0 so that the function will return the string of the colour naem
        return "blue"
    else:
        return "black"                 # if none of the conditions are satisfied then will return back Black

#FUNCTION FOR CONVERTION INTO SCREEN COORDINATES ON THE SCREEN
def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    screen_coord_x = (x_origin + (ratio) * x)               # stores the x coordinate after the conversion into screen coordinate
    screen_coord_y = (y_origin + (ratio) * y)               # stores the y coordinate after the conversion into screen coordinate

    return screen_coord_x, screen_coord_y                   # returns back the x and y coordinate after conversion

#FUNCTION FOR CALCULATING THE MINIMUM AND MAXIMUM VALUE OF X ON THE SCREEN
def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    screen_x_min = 0                                        # screen_x_min variable declared as 0 which is used for calculating the minimum value of x
    screen_x_max = 800                                      # screen_x_max variable declared as 800 which is used for calculating the maximum value of x

    x_solver1 = (screen_x_min - x_origin) / (ratio)         # to find out the minimum value for x
    x_solver2 = (screen_x_max - x_origin) / (ratio)         # to find out the maximum value for x

    minimum_x = int(floor(x_solver1))                       # Type conversion of the minimum x value also floor is used for finding out the largest integer not greater than x
    maximum_x = int(ceil(x_solver2))                        # Type conversion of the maximum x value also ceil is used for finding out the smallest integer not greater than x

    return minimum_x, maximum_x                             # returns back the minimum and maximum value of x

#FUNCTION FOR CALCULATING THE MINIMUM AND MAXIMUM VALUE OF Y ON THE SCREEN
def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    screen_y_min = 0                                        # screen_y_min variable declared as 0 which is used for calculating the minimum value of y
    screen_y_max = 600                                      # screen_y_min variable declared as 600 which is used for calculating the minimum value of y

    y_solver1 = (screen_y_min - y_origin) / (ratio)         # to find out the minimum value for y
    y_solver2 = (screen_y_max - y_origin) / (ratio)         # to find out the maximum value for y

    minimum_y = int(floor(y_solver1))                       # Type conversion of the minimum y value also floor is used for finding out the largest integer not greater than y
    maximum_y = int(ceil(y_solver2))                        # Type conversion of the minimum y value also floor is used for finding out the largest integer not greater than y

    return minimum_y, maximum_y                             # returns back the minimum and maximum value of x

#FUNCTION FOR DRAWING OUT THE LINE WITH THE TWO PAIRS OF COORDINATES
def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    pointer.penup()                                         # command to avoid the turtle to draw any non useful line while moving around
    pointer.goto(screen_x1,screen_y1)                       # command to move the turtle to those coordinates on the screen
    pointer.pendown()                                       # command to pull the pen down so that the turtle can start drawing while moving
    pointer.goto(screen_x2,screen_y2)                       # command to move the turtle to those coordinates on the screen and hence draws a line
    pointer.penup()                                         # command to avoid the turtle to draw any non useful line while moving around

#FUNCTION FOR DRAWING OUT THE TICKS ON THE X AXIS
def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    draw_line(pointer, screen_x, screen_y+adjustment_value_for_tick, screen_x, screen_y-adjustment_value_for_tick)     # command for drawing the ticks on the x axis by passing out the three parameters

#FUCNTION FOR DRAWING OUT THE LABELS(NUMBERS) ON THE AXIS
def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.goto(screen_x,screen_y-adjustment_value_for_labels)        # command to move the turtle to those coordinates on the screen that is below the ticks
    pointer.write(label_text, align="center")                          # command for writing out the out the numbers corresponding to each tick

#FUNCTION FOR DRAWING OUT THE TICKS ON THE Y AXIS
def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    draw_line(pointer, screen_x+adjustment_value_for_tick, screen_y, screen_x-adjustment_value_for_tick, screen_y)     # command for drawing the ticks on the y axis by passing out the three parameters

#FUCNTION FOR DRAWING OUT THE LABELS(NUMBERS) ON THE AXIS
def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.goto(screen_x-adjustment_value_for_labels,screen_y)         # command to move the turtle to those coordinates on the screen that is below the ticks
    pointer.write(label_text, align="center")                           # command for writing out the out the numbers corresponding to each tick

#FUNCTION FOR DRAWING OUT THE X AXIS
def draw_x_axis(pointer, x_origin, y_origin, ratio,):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    minimumValueOfx, maximumValueOfx = calc_minmax_x (x_origin, ratio)                                                  # calling out minmax_x function and storing the value returned by the function

    screenCordX1, screenCordY1 = calc_to_screen_coord(minimumValueOfx, 0, x_origin, y_origin, ratio)                    # conversion of minimum value of x into the screen coordinates y value specified as zero as its for the x axis
    screenCordX2, screenCordY2 = calc_to_screen_coord(maximumValueOfx, 0, x_origin, y_origin, ratio)                    # conversion of maximum value of x into the screen coordinates y value specified as zero as its for the x axis

    draw_line(pointer, screenCordX1, screenCordY1, screenCordX2, screenCordY2)                                          # used for drawing out the x axis from the minimum screen x value to the maximum screen x value

    for i in range(minimumValueOfx, maximumValueOfx + spacing, spacing):                                                # loop used for drawing out the ticks ranging from the minimum value of x to the maximum value of x with a spacing of 1 between each of the ticks
        screenCord_x, screenCord_y = calc_to_screen_coord(i, 0, x_origin, y_origin, ratio)                              # conversion of every coordinate value that variable i is looping through into the screen coordinates and storing them into screenCord_x and screenCord_y
        draw_x_axis_tick(pointer, screenCord_x, screenCord_y)                                                           # calling out the draw_x_axis_tick function by passing out the parameters screenCord_x and screenCord_y

    for i in range(minimumValueOfx, maximumValueOfx + spacing, spacing):                                                # loop used for drawing out the ticks ranging from the minimum value of x to the maximum value of x with a spacing of 1 between each of the ticks
        screenCord_x, screenCord_y = calc_to_screen_coord(i, 0, x_origin, y_origin, ratio)                              # conversion of every coordinate value that variable i is looping through into the screen coordinates and storing them into screenCord_x and screenCord_y
        draw_x_axis_label(pointer,screenCord_x, screenCord_y,i)                                                         # calling out the draw_label function to write the values to the corresponding ticks

#FUNCTION FOR DRAWING OUT THE Y AXIS
def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    minimumValueOfy, maximumValueOfy = calc_minmax_y(y_origin, ratio)                                                   # calling out minmax_y function and storing the value returned by the function
    screenCordX1, screenCordY1 = calc_to_screen_coord(0, minimumValueOfy, x_origin, y_origin, ratio)                    # conversion of minimum value of y into the screen coordinates y value specified as zero as its for the y axis
    screenCordX2, screenCordY2 = calc_to_screen_coord(0, maximumValueOfy, x_origin, y_origin, ratio)                    # conversion of maximum value of y into the screen coordinates y value specified as zero as its for the y axis

    draw_line(pointer, screenCordX1, screenCordY1, screenCordX2, screenCordY2)                                          # used for drawing out the y axis from the minimum screen x value to the maximum screen y value

    for i in range(minimumValueOfy, maximumValueOfy + spacing, spacing):                                                # loop used for drawing out the ticks ranging from the minimum value of y to the maximum value of y with a spacing of 1 between each of the ticks
        screenCord_x, screenCord_y = calc_to_screen_coord(0, i, x_origin, y_origin, ratio)                              # conversion of every coordinate value that variable i is looping through into the screen coordinates and storing them into screenCord_x and screenCord_y
        draw_y_axis_tick(pointer, screenCord_x, screenCord_y)                                                           # calling out the draw_x_axis_tick function by passing out the parameters screenCord_x and screenCord_y

    for i in range(minimumValueOfy, maximumValueOfy + spacing, spacing):                                                # loop used for drawing out the ticks ranging from the minimum value of y to the maximum value of y with a spacing of 1 between each of the ticks
        screenCord_x, screenCord_y = calc_to_screen_coord(0, i, x_origin, y_origin, ratio)                              # conversion of every coordinate value that variable i is looping through into the screen coordinates and storing them into screenCord_x and screenCord_y
        draw_y_axis_label(pointer,screenCord_x, screenCord_y,i)                                                         # calling out the draw_label function to write the values to the corresponding ticks

def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pointer.color(colour)                                                                               # for specifying the color of the curve that are to be drawn
    pointer.pensize("2")                                                                                # for specifying thr pointer size(thickness with which the curve will be drawn)
    min_x,max_x = calc_minmax_x(x_origin,ratio)                                                         # calling out minmax_x function and storing the value returned by the function
    x = min_x                                                                                           # used for looping the the function
    while(x<=max_x):                                                                # while loop for drawing out the expressions
        x1 = x                                                                      # Finding out the coordinates for drawing the expression (curves) and storing them in x1,x2,y1,y2
        x2 = x + delta
        y1 = calc(expr, x1)
        y2 = calc(expr, x2)
        screenx1,screeny1 = calc_to_screen_coord(x1,y1,x_origin,y_origin,ratio)    # conversion into screen coordinates
        screenx2,screeny2 = calc_to_screen_coord(x2,y2,x_origin,y_origin,ratio)
        draw_line(pointer,screenx1,screeny1,screenx2,screeny2)                    # calling out the draw line function to draw the curve
        x = x + delta                                                             # incrementation of the x variable otherwise an infinite loop would run

# YOU SHOULD NOT NEED TO CHANGE ANYTHING BELOW THIS LINE UNLESS YOU ARE DOING THE BONUS
def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)                                   # for calculating the expression using eval() function
#SETUP FUNCTION FOR THE TURTLE SCREEN TO SHOW UP
def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer
#MAIN FUNCTION WHICH CALLS ALL THE OUTHER FUNCTIONS PREVIUSOULY DEFINED AND COMPLETED
def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))          # user input is taken for x_origin and y_origin variables
    ratio = int(input("Enter ratio of pixels per step: "))

    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1
main()
turtle.exitonclick()
