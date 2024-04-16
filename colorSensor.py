 #!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():
 
       def __init__(self):
              # tégla
              self.ev3 = EV3Brick()
              # motorok
              self.jm = Motor(Port.B)
              self.bm = Motor(Port.C)
              self.km = Motor(Port.A)
              # szenzorok
              self.cs = ColorSensor(Port.S3)
              self.ts = TouchSensor(Port.S1)
              self.gs = GyroSensor(Port.S2)
              self.us = UltrasonicSensor(Port.S4)
              #self.ir = InfraredSensor(Port.S4)
              self.robot = DriveBase(self.jm, self.bm, 55, 115)
              self.ido = StopWatch()

       def rgb(self):
               #Sárga: Red: 53, green: 47, blue: 19
               #Piros red: 32, green:6, blue:5
               #Zold: 
               print(self.cs.rgb())



       def ambient(self):
              #Sárga: -1
              #Piros: 3
              # 
              print(self.cs.ambient())
              pass

       def feladat(self):
              szinLista =  []
              if(self.cs.ambient() >= 4):
                     self.robot.drive(100,0)
                     self.ido.reset()
                     while(self.ido.time() < 3000):
                            szin = self.cs.color()
                            if(szin != Color.WHITE):
                                   if szin not in szinLista:
                                          szinLista.append(szin)
                     self.robot.stop(Stop.BRAKE)      
              wait(3000)
              print(szinLista)                        

