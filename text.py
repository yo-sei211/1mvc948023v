#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

lm = Motor(Port.A)
rm = Motor(Port.D)
Mlm = Motor(Port.C)
Mrm = Motor(Port.B)

robot = DriveBase(lm, rm, 70, 120)

Lr = ColorSensor(Port.S4)
Rr = ColorSensor(Port.S1)
R2r = ColorSensor(Port.S3)

corP = 0
zure1 = 0
corD = 0
c1 = Lr.reflection()
c2 = Rr.reflection()


while lm.angle() <= 180:
    lm.run(600)
    rm.run(-600)

while c1 + c2 >= 80:
    c1 = Lr.reflection()
    c2 = Rr.reflection()
    lm.run(-200)
    rm.run(-200)
    print(c1 + c2)

lm.reset_angle(0)
rm.reset_angle(0)

while lm.angle() >= -200:
   c1 = Lr.reflection()
   c2 = Rr.reflection()
   zure1 = corP
   corP = c1 - c2
   corD = corP - zure1
   GacorD = corD * 1
   GacorP = corP * -1
   robot.drive(-60, GacorP + GacorD)
   ev3.screen.print(lm.angle())

while True: 
   c1 = Lr.reflection()
   c2 = Rr.reflection()
   zure1 = corP
   corP = c1 - c2
   corD = corP - zure1
   GacorD = corD * 1
   GacorP = corP * -0.8
   robot.drive(-300, GacorP + GacorD)
   ev3.screen.print(GacorD)

