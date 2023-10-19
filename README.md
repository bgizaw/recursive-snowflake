# CS051P Lab Assignments: Recursive Graphics

**Author:** Biruk Gizaw

## Overview

This repository contains Python code for drawing various geometric shapes using recursion and the Turtle graphics library. The primary goal of this assignment is to help you gain a deeper understanding of recursion and to write recursive functions that produce interesting graphical patterns.

## Description

### draw_triangle
The `draw_triangle` function draws an equilateral triangle with a specified side length and color. It uses the Turtle graphics library to create the triangle and return to the original position and heading.

### draw_polygon
The `draw_polygon` function draws a polygon with a user-defined number of sides, each of a specified length. It uses the Turtle graphics library to draw polygons with various numbers of sides.

### stairs
The `stairs` function recursively draws a pattern of squares of different sizes, creating a staircase effect. It takes the starting coordinates and the size of the first square as input and returns the total number of squares drawn.

### snowflake
The `snowflake` function recursively draws a snowflake pattern. It uses eight branches to form the snowflake, and the size of the branches decreases with each recursive call. The function returns the total number of lines drawn.

## Requirements
- Python 3.x
- Turtle graphics library (usually included with Python)

## Usage
You can use this code to experiment with recursive graphics and explore different shapes and patterns. To use the functions in your own Python program, you need to import them from the provided script.

Example:

```python
from recursive_graphics import draw_triangle, draw_polygon, stairs, snowflake

# Usage of the functions
# ...

# Don't forget to call done() to preserve the display after drawing.
done()
