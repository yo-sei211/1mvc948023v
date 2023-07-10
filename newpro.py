#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.

lm = Motor(Port.A)
rm = Motor(Port.D)
Mlm = Motor(Port.B)
Mrm = Motor(Port.C)

robot = DriveBase(lm, rm, 70, 120)

Lr = ColorSensor(Port.S4)
Rr = ColorSensor(Port.S1)
R2r = ColorSensor(Port.S3)
sensor = Ev3devSensor(Port.S2)
def port():
    global Lr
    global Rr
    global R2r
    global sensor
    global lm
    global rm
    global Mlm
    global Mrm
port()
corP = 0
zure1 = 0
corD = 0
c1 = Lr.reflection()
c2 = Rr.reflection()

c3 = R2r.reflection()
s3 = R2r.color() 
def num():
    global num1
    global num2
    global num3
    global num4
num()
def bl():
    global bl1
    global bl2
    global bl3
    global bl4
    global bl5
    global bl6
    global bl7
    global bl8
bl()
def pd():
    global zure1
    global corP
    global clrD
    global GacorP
    global GacorD
    global num1
    global num2
    global num3
    global num4
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    s3 = R2r.color() 
    zure1 = corP
    corP = c1 - c2
    corD = corP - zure1
    GacorD = corD * 1
    GacorP = corP * -0.3
    robot.drive(-160, GacorP)

    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
def pd2():
    global zure1
    global corP
    global clrD
    global GacorP
    global GacorD
    global num1
    global num2
    global num3
    global num4
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    s3 = R2r.color() 
    zure1 = corP
    corP = c1 - c2
    corD = corP - zure1
    GacorD = corD * 1
    GacorP = corP * -0.7
    robot.drive(-300, GacorP)

    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    print(num4)
def pd3():
    global zure1
    global corP
    global clrD
    global GacorP
    global GacorD
    global num1
    global num2
    global num3
    global num4
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    s3 = R2r.color() 
    zure1 = corP
    corP = c1 - c2
    corD = corP - zure1
    GacorD = corD * 1
    GacorP = corP * -0.5
    robot.drive(-100, GacorP)

    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    print(num4)
def pd4():
    global zure1
    global corP
    global clrD
    global GacorP
    global GacorD
    global num1
    global num2
    global num3
    global num4
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    s3 = R2r.color() 
    zure1 = corP
    corP = c1 - c2
    corD = corP - zure1
    GacorD = corD * 1
    GacorP = corP * 0.25
    robot.drive(100, GacorP)

    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    print(num4)
def red1():
    while lm.angle() <= 290:
        lm.run(250)
        rm.run(0)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -60:
        lm.run(-400)
        rm.run(-400)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    """
    while lm.angle() <= 130:
        lm.run(300)
        rm.run(-300)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    """
    while lm.angle() >= -145:
        lm.run(-350)
        rm.run(350)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -700:
        pd3()
    while True:
        pd2()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 95:
            break
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(-200,125,Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() >= -270:
        lm.run(-400)
        rm.run(0)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -625:
        lm.run(-500)
        rm.run(-500)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
def red2():
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    while lm.angle() <= 139:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() <= 170:
        lm.run(200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -205:
        lm.run(-200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0)    
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    while lm.angle() <= 127:
        lm.run(200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    while lm.angle() >= -500:
        pd3()
    while True:
        pd2()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 95:
            break
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(-200,125,Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() >= -10:
        lm.run(-400)
        rm.run(-400)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -270:
        lm.run(-400)
        rm.run(0)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -625:
        lm.run(-500)
        rm.run(-500)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
def red4():
    while lm.angle() <= 290:
        lm.run(250)
        rm.run(0)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -60:
        lm.run(-400)
        rm.run(-400)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    """
    while lm.angle() <= 130:
        lm.run(300)
        rm.run(-300)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    """
    while lm.angle() >= -145:
        lm.run(-350)
        rm.run(350)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -700:
        pd3()
    while True:
        pd2()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 95:
            break
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(-200,125,Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() >= -270:
        lm.run(-400)
        rm.run(0)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -625:
        lm.run(-500)
        rm.run(-500)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
def red3():
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    while lm.angle() <= 139:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.run_angle(200,100,Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() <= 170:
        lm.run(200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -205:
        lm.run(-200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0)    
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    while lm.angle() <= 127:
        lm.run(200)
        rm.run(-200)
    lm.reset_angle (0) 
    rm.reset_angle (0) 
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 95:
            break
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.run_angle(-200,125,Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    while lm.angle() >= -10:
        lm.run(-400)
        rm.run(-400)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -270:
        lm.run(-400)
        rm.run(0)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -625:
        lm.run(-500)
        rm.run(-500)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
def set1p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        lm.run(220)
        rm.run(220)
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -115:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -115:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 325:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -40:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 80:
        lm.run(200)
        rm.run(200)
    while lm.angle() >= -50:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -80:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 90:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -20:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -135:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -650:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set2p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        lm.run(220)
        rm.run(220)
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -115:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -115:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while rm.angle() >= -550:
        lm.run(0)
        rm.run(-500)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 650:
        lm.run(650)
        rm.run(0)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set3p():
    while lm.angle() <= 50:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 170:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -217:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 263:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 133:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -80:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 720:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -136:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 262:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 190:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -524:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set4p():
    while lm.angle() <= 103:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 165:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -217:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() >= -140:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -460:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 126:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 280:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 138:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -135:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 95:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set5p():
    while lm.angle() >= -560:
        lm.run(-200)
        rm.run(-210)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 115:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -175:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() >= -113:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 233:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 130:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 5:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 150:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -115:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set6p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -250:
        pd3()
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 125:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 614:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() >= -15:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 156:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -202:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -135:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -524:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set7p():
    while lm.angle() <= 98:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 160:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -175:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() >= -113:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 200:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 150:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)   
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 20:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 171:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -50:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set8p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        lm.run(200)
        rm.run(200)
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 147:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -63:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 512:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -130:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -126:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 302:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 180:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -20:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set9p():
    while lm.angle() >= -232:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 22:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -5:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 18:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 270:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -530:
        pd3()
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -180:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 150:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -80:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set10p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        lm.run(200)
        rm.run(200)
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -120:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() >= -10:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 155:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -280:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -160:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set11p():
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 300:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while True:
        lm.run(200)
        rm.run(200)
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print (c1 + c2)
        if c1 + c2 <= 60:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -125:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -100:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 660:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 100:
        lm.run(200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 156:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -202:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -145:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -524:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
def set12p():
    while lm.angle() >= -300:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() <= 140:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mrm.angle() >= -251:
        Mrm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    Mrm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mrm.reset_angle (0)
    while lm.angle() <= 150:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -138:
        lm.run(-200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -280:
        pd3()
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -190:
        lm.run(-200)
        rm.run(200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while Mlm.angle() >= -120:
        Mlm.run(-100)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    Mlm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    Mlm.reset_angle (0)
    while lm.angle() <= 150:
        lm.run(200)
        rm.run(-200)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.stop (Stop.BRAKE)
    rm.stop (Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)
    while lm.angle() >= -200:
        pd3()
    while True:
        pd3()
        c1 = Lr.reflection()
        c2 = Rr.reflection()
        print(c1 + c2)
        if c1 + c2 <= 65:
            break
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    robot.stop(Stop.BRAKE)
    lm.reset_angle (0) 
    rm.reset_angle (0)

ev3.speaker.beep()

while True:
    set12p()
    break
while lm.angle() >= -25:
    lm.run(-400)
    rm.run(-400)
lm.reset_angle (0) 
rm.reset_angle (0)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)
rm.run_angle(-490,350,Stop.BRAKE)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -125:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl1 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl1 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl1 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl2 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl2 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl2 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl3 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl3 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl3 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl4 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl4 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl4 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -155:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl5 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl5 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl5 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl6 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl6 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl6 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl7 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl7 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl7 = 0
        break
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -60:
    pd3()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
wait(100)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 100:
        bl8 = 1
        ev3.speaker.play_notes(['C4/4'],500)
        break
    elif num4 >= 70 and num4 <= 220:
        bl8 = 2
        ev3.speaker.play_notes(['D4/4'],500)
        break
    else:
        bl8 = 0
        break
#色認識終わり。
lm.reset_angle (0) 
rm.reset_angle (0)
Mlm.reset_angle (0) 
Mrm.reset_angle (0)
Mlm.run_angle(300,54,Stop.BRAKE)
Mrm.run_angle(300,54,Stop.BRAKE)
while True:
    lm.run(-260)
    rm.run(-260)
    if R2r.color() == Color.RED:
        break
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() <= 19:
    lm.run(100)
    rm.run(100)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
Mlm.reset_angle (0) 
Mrm.reset_angle (0)
Mlm.run_angle(300,133,Stop.BRAKE)
Mrm.run_angle(300,133,Stop.BRAKE)
Mlm.stop (Stop.BRAKE)
Mrm.stop (Stop.BRAKE) 
Mlm.stop (Stop.BRAKE)
Mrm.stop (Stop.BRAKE) 
Mlm.stop (Stop.BRAKE)
Mrm.stop (Stop.BRAKE) 
lm.reset_angle (0) 
rm.reset_angle (0)
Mlm.reset_angle (0) 
Mrm.reset_angle (0)
while lm.angle() >= -106:
    lm.run(-100)
    rm.run(-100)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)
Mlm.run_time(320,1000,Stop.BRAKE)
lm.reset_angle (0) 
rm.reset_angle (0)
Mlm.reset_angle (0) 
Mrm.reset_angle (0)
while lm.angle() <= 200:
    lm.run(400)
    rm.run(400)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE)  
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() >= -5:
    lm.run(-400)
    rm.run(400)
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.stop (Stop.BRAKE)
rm.stop (Stop.BRAKE) 
lm.reset_angle (0) 
rm.reset_angle (0)
#ここから
while lm.angle() >= -600:
    pd3()
while lm.angle() >= -1270:
    pd2()
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
lm.reset_angle (0) 
rm.reset_angle (0)
while True:
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    if num1 >= 20:
        ev3.speaker.play_notes(['C4/4'],500)
        red1()
        break
    else:
        while lm.angle() >= -140:
            lm.run(-350)
            rm.run(-350)
            print(lm.angle())
        lm.reset_angle (0) 
        rm.reset_angle (0)
        rm.run_angle(-500,325,Stop.BRAKE)
        lm.reset_angle (0) 
        rm.reset_angle (0)
        while lm.angle() >= -165:
            lm.run(-200)
            rm.run(-200)
        lm.stop (Stop.BRAKE)
        rm.stop (Stop.BRAKE)
        lm.reset_angle (0) 
        rm.reset_angle (0)
        while True:
            r= sensor.read('RGB')

            # Print results
            s = ("{0}".format(r))
            numbers = [int(number) for number in s.strip('()').split(', ')]
            num1, num2, num3, num4 = numbers
            if num1 >= 10:
                ev3.speaker.play_notes(['C4/4'],500)
                red2()
                break
            else:
                lm.stop (Stop.BRAKE)
                rm.stop (Stop.BRAKE)
                while lm.angle() <= 300:
                    lm.run(400)
                    rm.run(-400)
                lm.reset_angle (0) 
                rm.reset_angle (0)
                while lm.angle() >= -150:
                    lm.run(-400)
                    rm.run(-400)
                lm.reset_angle (0) 
                rm.reset_angle (0)    
                lm.stop (Stop.BRAKE)
                rm.stop (Stop.BRAKE)
                while lm.angle() <= 20:
                    lm.run(400)
                    rm.run(-400)
                lm.reset_angle (0) 
                rm.reset_angle (0) 
                lm.stop (Stop.COAST)
                rm.stop (Stop.COAST)
                while lm.angle() >= -365:
                    pd3()
                robot.stop(Stop.BRAKE)
                robot.stop(Stop.BRAKE)
                robot.stop(Stop.BRAKE)
                lm.reset_angle (0) 
                rm.reset_angle (0)
                while True:
                    r= sensor.read('RGB')

                    # Print results
                    s = ("{0}".format(r))
                    numbers = [int(number) for number in s.strip('()').split(', ')]
                    num1, num2, num3, num4 = numbers
                    if num1 >= 10:
                        ev3.speaker.play_notes(['C4/4'],500)
                        red4()
                        break
                    else:
                        while lm.angle() >= -180:
                            lm.run(-200)
                            rm.run(-200)
                            print(lm.angle())
                        lm.reset_angle (0) 
                        rm.reset_angle (0)
                        rm.run_angle(-200,344,Stop.BRAKE)
                        lm.reset_angle (0) 
                        rm.reset_angle (0)
                        while lm.angle() >= -165:
                            lm.run(-200)
                            rm.run(-200)
                        lm.stop (Stop.BRAKE)
                        rm.stop (Stop.BRAKE)
                        lm.reset_angle (0) 
                        rm.reset_angle (0)
                        red3()
                        break
                    break
                break
            break        
        break
    break
#赤回収終了。
lm.reset_angle (0) 
rm.reset_angle (0)
while lm.angle() <= 297:
    lm.run(300)
    rm.run(300)
lm.reset_angle (0) 
rm.reset_angle (0)
lm.stop (Stop.COAST)
rm.stop (Stop.COAST)
while lm.angle() >= -109:
    lm.run(-200)
    rm.run(200)
while lm.angle() >= -200:
    pd3()
while True:
    pd3()
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    print(c1 + c2)
    if c1 + c2 <= 95:
        break
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
lm.reset_angle (0) 
rm.reset_angle (0)
Mrm.run_time(820,1000,Stop.BRAKE)
Mlm.reset_angle (0) 
Mrm.reset_angle (0)
ev3.speaker.play_notes(['C4/4'],500)
while True:
    if bl2 == 1 and bl3 == 2:
        set1p()
        break
    elif bl2 == 1 and bl4 == 2:
        set2p()
        break
    elif bl2 == 2 and bl3 == 1:
        set3p()
        break
    elif bl2 == 2 and bl4 == 1:
        set4p()
        break
    elif bl3 == 2 and bl4 == 1:
        set5p()
        break
    elif bl3 == 1 and bl4 == 2:
        set6p()
        break
    elif bl1 == 1 and bl2 == 2:
        set7p()
        break
    elif bl1 == 1 and bl3 == 2:
        set8p()
        break
    elif bl1 == 1 and bl4 == 2:
        set9p()
        break
    elif bl1 == 2 and bl2 == 1:
        set10p()
        break
    elif bl1 == 2 and bl3 == 1:
        set11p()
        break
    elif bl1 == 2 and bl4 == 1:
        set12p()
        break
    break