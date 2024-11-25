from turtle import *
from math import *
import pyautogui
import time
from numpy import interp
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial(None, 115200, timeout=None)
ports_list = []

#region Setup for Turtle
# t = Turtle()
# t.screen.screensize(1920,1080)
# t.screen.setup(width = 1.0, height = 1.0)
# t.screen.bgcolor("Black")
# t.color("White")
# t.speed(0)
# t.hideturtle()
#endregion

#region Initialize starting variables
screen_size = pyautogui.size()
original_pos_x = [0, screen_size[0]]
mapped_pos_x = [0,1000]
original_pos_y = [0, screen_size[1]]
mapped_pos_y = [0,1000]

#get availble ports
for one in ports:
    ports_list.append(str(one))
    print(str(one))

com = input("Input arduino port: ")

for i in range(len(ports)):
    if ports_list[i].startswith("COM" + str(com)):
        use = "COM" + str(com)

serial_inst.baudrate = 115200 # Must match with arduino baudrate
serial_inst.port = use
serial_inst.open()

# l1 = float(input("Input the length of arm 1: ")) #Arm length 1
# l2 = float(input("Input the length of arm 2: ")) #Arm length 2
l1 = 500
l2 = 500
#endregion

time.sleep(1)

def create_arm():
    flip = [False,False]        
    #Find mouse pos and map to turtle
    mouse_pos = pyautogui.position()
    fx = interp(mouse_pos[0],original_pos_x,mapped_pos_x) #final x position
    fy = interp(screen_size[1]-mouse_pos[1],original_pos_y,mapped_pos_y) #final y position


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
        a1_2 = degrees(atan(fy/fx))
        a2_1 = 0
        a2_2 = 0
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

        a1_1 = round(degrees(a1_1))
        a1_2 = round(degrees(a1_2))
        a2_1 = round(degrees(a2_1))
        a2_2 = round(degrees(a2_2))

    #region Draws out arms
    # t.color("Red")
    # t.left(a1_1)
    # t.forward(l1)
    # t.color("Red3")
    # t.left(a2_1)
    # t.forward(l2)

    # t.penup()
    # t.home()
    # t.pendown()
    # t.clear()
    #endregion

    return [a1_1,a2_1]

def send_serial_data(a1,a2):
    a1 = int(a1)
    a2 = int(a2)
    
    if a2<=0:
        a2+= 180

    buffer = ""
    msg_1 = ""
    msg_2 = ""

    if abs(a1) < 100:
        buffer += "0"
        if abs(a1) < 10:
            buffer += "0"
    msg_1 = buffer + str(a1)
    buffer = ""

    if abs(a2) < 100:
        buffer = "0"
        if abs(a2) < 10:
            buffer += "0"
    msg_2 = buffer + str(a2)

    cmd = msg_1+msg_2
    print("angle 1: " + str(abs(a1)))
    print("angle 2: " + str(abs(a2)))
    print("Sent data to arduino: " + str(cmd))
    serial_inst.write(cmd.encode("utf-8"))
    Timer = time.time()
    print("Data sent")
    data = serial_inst.readline().decode('utf-8').strip()
    print("Recieved Data: " + str(data))
    print("Send & recieve took: " + str(time.time()-Timer))
    # serial_inst.write(input("input angle: ").encode("utf-8"))
    
try:
    while True:
        angles = create_arm()
        send_serial_data(angles[0], angles[1])
except KeyboardInterrupt:
    exit

