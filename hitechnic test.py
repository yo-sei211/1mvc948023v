#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor
ev3 = EV3Brick()
sensor = Ev3devSensor(Port.S2)
num1 = 0
R2r = ColorSensor(Port.S3)
s3 = R2r.color() 

while True:
    s3 = R2r.color() 
    # Read the raw RGB values
    r= sensor.read('RGB')

    # Print results
    s = ("{0}".format(r))
    numbers = [int(number) for number in s.strip('()').split(', ')]
    num1, num2, num3, num4 = numbers
    sumnum = num1 + num2 + num3 + num4
    if sumnum >= 100 and sumnum <= 500:
        print("black")
    elif sumnum >= 700:
        print("white")
    else:
        print("air")
