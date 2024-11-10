from turtle import *
from math import *
import pyautogui

t = Turtle()
t.screen.screensize(1920,1080)
t.screen.setup(width = 1.0, height = 1.0)
t.screen.bgcolor("Black")
t.color("White")

fx = 100
fy = 100
l1 = 300
l2 = 200


constant = fx**2 + fy**2 + l1**2 - l2**2 
cos_coef = 2*fx*l1
sin_coef = 2*fy*l1

print("coefficients")
print(cos_coef)
print(sin_coef)


a1_1 = atan(sin_coef/cos_coef) + acos(constant/(sqrt(cos_coef**2 + sin_coef**2)))
a1_2 = atan(sin_coef/cos_coef) - acos(constant/(sqrt(cos_coef**2 + sin_coef**2)))
print(degrees(a1_1))

a2_1 = atan((fy - l1*sin(a1_1)) / (fx - l1*cos(a1_1))) - a1_1
a2_2 = atan((fx - l1*cos(radians(a1_2))) / (fy - l1*sin(radians(a1_2)))) - a1_2
print(degrees(a2_1))


a1_1 = degrees(a1_1)
a1_2 = degrees(a1_2)
a2_1 = degrees(a2_1)
a2_2 = degrees(a2_2)

t.left(a1_1)
t.forward(l1)
t.left(a2_1)
t.forward(l2)

t.penup()
t.goto(0,0)
t.pendown()
t.goto(fx,fy)



exitonclick()