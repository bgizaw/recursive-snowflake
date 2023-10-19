"""
    CS051P Lab Assignments: Recursive Graphics

    Name: Biruk Gizaw

    Date:   10/17/2023

    The goal of this assignment is to familiarize you with recursion,
    including thinking and writing recursive functions.
"""
from turtle import *
from math import sqrt


def draw_triangle(length, color):
    """
    Draw equilateral triangle, from the current position.
    :param length: (int) side length in pixels
    :param color: (string) line color

    end up in original position and heading
    """
    # set color and drop the pen
    pencolor(color)
    pendown()

    # three sides, w/120 degree exterior angles
    # Note: this function demostrates poor style (it uses repeated code)
    forward(length)
    left(120)
    forward(length)
    left(120)
    forward(length)
    left(120)

    # we should now be at our original position/heading


def draw_polygon(n, length):
    """
    draw a polygon with n sides that are the length the user chooses

    :param n: (int) number of sides on polygon
    :param length: (int) length of each side of the polygon
    :return: None
    """
    # find the angle the turtle needs to turn after each lines by dividing 360 by the number of sides
    turn_angle = 360/n
    for i in range(n):
        forward(length)
        left(turn_angle)


def stairs(x, y, length):
    """
    Draw recursive stairs using squares of different sizes

    :param x: (int) x coordinates
    :param y: (int) y coordinates
    :param length: (int) length of the sides of the first square
    :return: (int) total number of squares drawn
    """
    total1 = 0
    total2 = 0
    if length <= 10:
        return 0
    else:
        speed(0.1)
        penup()
        goto(x, y)
        pendown()
        draw_polygon(4, length)
        total1 += stairs(x + length, y, length/2)
        total2 += stairs(x, y + length, length/2)
        return 1 + total1 + total2





def main_part1():
    """
    draw polygons with different numbers of sides and print out the recursive staircase

    """
    # draw a dot of size 5 in the center of the screen
    # dot(5)

    # fancy geometry to calculate the starting point of an equilateral triangle at
    # the center of the screen
    # If you understand the math, great! If not, that's fine. Don't spend time 
    # worrying about it. This isn't a geometry class. 
    # side_len = 60
    # triangle_height = sqrt(side_len**2 - (side_len/2)**2) # use Pythagorean thm
    # centroid_height = triangle_height/3  # centroid is 1/3 up the height
    # y_init = -1 * centroid_height
    # x_init = -1 * (side_len/2)

    # draw a single triangle of size 60 in the center of the screen
    # penup()
    # setposition(x_init,y_init)
    # pendown()
    # setheading(0)
    # draw_triangle(60, "black")

    # Try to make them not overlap!
    penup()
    goto(-300, 100)
    pendown()
    draw_polygon(3, 100)

    penup()
    goto(-100, 100)
    pendown()
    draw_polygon(4, 100)

    penup()
    goto(50, 100)
    pendown()
    draw_polygon(6, 50)

    penup()
    goto(200, 100)
    pendown()
    draw_polygon(12, 30)

    penup()
    goto(0, -200)
    pendown()
    draw_polygon(30, 20)

    print(stairs(-200, -200, 200))


    # hide turtle and preserve the display
    hideturtle()
    done()


def snowflake(x, y, size):
    """
    Draw a snowflake using recursion

    :param x: (int) x coordinates
    :param y: (int) y coordinates
    :param size: (int) distance turtle pen will draw
    :return total: (int) number of lines that have been drawn
    """
    total = 0

    # draw a red dot in every instance where the size of the lines is less than 5
    if size <= 5:
        for i in range(4):
            penup()
            goto(x, y)
            pendown()
            dot(5, "red")
        return 0
    else:
        # draws each section of lines in the snowflake
        for i in range(8):
            penup()
            goto(x, y)
            pendown()
            forward(size)
            penup()
            goto(x, y)
            pendown()
            left(45)
        total += 8

        # all of these totals added together gets our number of lines
        total += snowflake(x + size, y, size / 3)
        total += snowflake(x, y + size, size / 3)
        total += snowflake(-(x + size), y, size / 3)
        total += snowflake(x, -(y + size), size / 3)
        return total


def main():
    """
    Call snowflake function and hide pen after finishing
    """
    speed(0)
    print(snowflake(0, 0, 100))
    hideturtle()
    done()


if __name__ == '__main__':
    # main_part1()  # comment this out after you check-in for part 1
    main()  # uncomment this after you check-in for part 1
