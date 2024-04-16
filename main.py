#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import colorSensor



oaraimunka=ColorSensor.Feladatok()


peldany = colorSensor.Feladatok()
#peldany.rgb()  
#peldany.ambient()
peldany.feladat()

ev3.speaker.beep()
