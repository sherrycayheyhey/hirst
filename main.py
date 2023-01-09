# file, settings, Project: whaterever, Python Interpreter, + sign to install module/package
import colorgram


# *************** this code extracts the original colors, but it only needs to run once ***************
# # extract 30 colors form the image, this returns color objects
# colors = colorgram.extract('lfstickrs.jpg', 30)
#
# # convert the color objects into rgb colors
# rgb_colors = []
# for color in colors:
#     # get the rgb tuple
#     rgb = color.rgb
#
#     # separate each color from the string label in the tuple
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#
#     # recombine the values
#     rgb_tuple = (red, green, blue)
#
#     # add the tuple to the list
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)
# ***************************************************************************************************************

from turtle import Turtle, Screen
import random

# optional: check list and delete any excessive, boring colors
color_list = [(210, 161, 84), (130, 63, 105), (71, 102, 142), (234, 210, 97), (206, 82, 119), (147, 159, 71), (63, 27, 56), (200, 136, 156), (98, 42, 82), (132, 158, 179), (81, 126, 99), (99, 148, 108), (131, 167, 136), (237, 198, 210), (37, 39, 63), (233, 166, 183), (195, 97, 79), (96, 126, 168), (51, 53, 102), (196, 212, 225), (113, 42, 33), (200, 221, 210), (84, 143, 158), (227, 174, 167), (87, 77, 22), (31, 51, 40), (175, 202, 188)]


tina = Turtle()
tina.shape("turtle")
tina.speed(0)

# create the screen, set the screen color-mode in order to use rgb 0-255 numbers
screen = Screen()
screen.colormode(255)

# go to starting position
tina.penup()
tina.goto(-300, 300)

# 10x10 dot matrix, 20 size dot, 50 spaces apart
# draw a row of dots
for row in range(10):
    # 70 down, back to x=-300
    tina.goto(-300, row * 50 - 300)
    for dot in range(10):
        tina.dot(20, random.choice(color_list))
        tina.forward(50)

# keep the screen open until clicked
screen.exitonclick()

