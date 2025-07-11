from turtle import *
from math import *
import pyautogui

#Basic setup for Turtle
t = Turtle()
t.screen.screensize(1920,1080)
t.screen.setup(width = 1.0, height = 1.0)
t.screen.bgcolor("Black")
t.color("White")

#Initialize starting variables

fx = 350 #final x position
fy = 10 #final y position
l1 = 300 #Arm length 1
l2 = 500 #Arm length 2

final_pos = (fx, fy)
flip = [False,False] 

#Keeps track of inverting for later
if fx<0:
    fx*=-1
    flip[0] = True
if fy<0:
    fy*=-1
    flip[1] = True

#Checks if final distance is farther than combined arm length
if l1+l2<sqrt(fx**2+fy**2):
    a1_1 = degrees(atan(fy/fx))
    a2_1 = 0
else:
    constant = fx**2 + fy**2 + l1**2 - l2**2 
    cos_coef = 2*fx*l1
    sin_coef = 2*fy*l1

    #Case for if any final pos is a zero
    if cos_coef == 0:
        a1_1 = asin(constant/sin_coef)
        a1_2 = pi - asin(constant/sin_coef)
    else:
        a1_1 = atan(sin_coef/cos_coef) + acos(constant/(sqrt(cos_coef**2 + sin_coef**2)))
        a1_2 = atan(sin_coef/cos_coef) - acos(constant/(sqrt(cos_coef**2 + sin_coef**2)))

    a2_1 = atan2((fy - l1*sin(a1_1)), (fx - l1*cos(a1_1))) - a1_1
    a2_2 = atan2((fy - l1*sin(a1_2)), (fx - l1*cos(a1_2))) - a1_2

    #Invert arm depending on flip variable
    if flip[0] and flip[1]:
        a1_1 = pi+a1_1
        a1_2 = pi+a1_2
    elif flip[0]:
        a1_1 = pi-a1_1
        a1_2 = pi-a1_2
        a2_1 = 2*pi-a2_1
        a2_2 = 2*pi-a2_2
    elif flip[1]:
        a1_1 = 2*pi-a1_1
        a1_2 = 2*pi-a1_2
        a2_1 = 2*pi-a2_1
        a2_2 = 2*pi-a2_2

    a1_1 = degrees(a1_1)
    a1_2 = degrees(a1_2)
    a2_1 = degrees(a2_1)
    a2_2 = degrees(a2_2)

#Draws out arms
t.color("Red")
t.left(a1_1)
t.forward(l1)
t.color("Red3")
t.left(a2_1)
t.forward(l2)

t.penup()
t.home()
t.pendown()

t.color("Aquamarine")
t.left(a1_2)
t.forward(l1)
t.color("Aquamarine4")
t.left(a2_2)
t.forward(l2)

t.color("White")
t.penup()
t.home()
t.pendown()
t.goto(final_pos[0],final_pos[1])

exitonclick()