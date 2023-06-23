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
    robot.drive(-150, GacorP)

    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers

while True:
    pd()
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    print(c1 + c2)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)
robot.stop(Stop.BRAKE)