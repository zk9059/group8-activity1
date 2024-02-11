"""
group 8
Done by Khaled Abusharbain (contribution: hexagon shape, pattern function, main function),
 zarak khan(square function shape), nour abdelwahed  (circle function)
 This module code has multiple functions with 3 different shapes to create a pattern of 3 shapes , it allows the user to choose his own shape color 
 and border.
"""

import turtle


def circle(turta, circle_color, border_color): # function to draw circle shape filled with circle color with its border color
    turta.begin_fill() # begin fill of circle
    turta.color(circle_color, border_color)
    turta.circle(49) #
    turta.end_fill()    


def hexagon(turta, hexagon_color, border_color): # function to draw hexagon shape filled with hexa color with border color 
    turta.begin_fill() # start filling hexagon shape  
    turta.color(hexagon_color, border_color)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.right(60)
    turta.forward(50)
    turta.end_fill()

def square(turta, square_color, border_color): # square function that draws a square shape and fills color
    turta.begin_fill()
    turta.color(square_color, border_color)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.forward(90)
    turta.right(90)
    turta.end_fill()

def setPos(turta, x, y):
    turta.up() # turtle pen up so when it moves it doesnt trace
    turta.goto(x,y) # moves to specified x and y which it will be used later
    turta.down() # puts the pen down to draw when it moves after being in the specified x and y

def pattern(turta, x, y, border_color, circle_color, hexagon_color, square_color):
    setPos(turta, x, y) # sets the postition of the turta
    hexagon(turta ,border_color, hexagon_color) # calls hexagon function, with its border color and its own hexa color
    setPos(turta, x+100, y-90) # then moves 100 units to the right and 90 down from hexagon position
    circle(turta ,border_color, circle_color) # calls circle function, with its border color and its own circle color choosen
    setPos(turta, x+180, y) # then it moves 180 units to the right from the circle position
    square(turta, border_color, square_color) # calls the square function with the border color and its own color 

def main():
    border_color=input("the color of  the shape borders: ") # user chooses the color of the border
    hexagon_color=input("Enter the color of the hexagon: ") # user chooses the color for hexagon shape
    circle_color=input("Enter the color of the circle: ")   # user chooses the color for circle shape 
    square_color=input("Enter the color of the square: ")   # user chooses the color for square shape
    turta = turtle.Turtle() # initializing turtle
    screen = turtle.Screen() # turtle screen
    turta.pensize(2) # size of the pen
    turta.pencolor(border_color) # here the color of the pen is the border color asked from the user
    screen.bgcolor("Light Blue") # background color of the screen as required 
    
        
    pattern(turta, -250, 230, border_color, circle_color, hexagon_color, square_color) #calls the pattern function above with certian x and y
    pattern(turta, -140, 120, border_color, circle_color, hexagon_color, square_color) # calls the pattern function to create the second line pattern
    pattern(turta, -30, 0, border_color, circle_color, hexagon_color, square_color)  #calls the pattern function to create the third line pattern
    turtle.exitonclick() # exit on click when done.

main() #calls the main function