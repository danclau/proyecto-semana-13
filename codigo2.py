import RPi.GPIO as GPIO ## import GPIO library
import time ## Import 'time' library. Alows us to use 'sleep'

from tkinter import *

GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 7 to OUT

GPIO.setwarnings(True)

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, text="Cerrar", fg="red", command=quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,text="Prender", command=self.prender)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,text="Apagar", command=self.apagar)
    self.slogan.pack(side=LEFT)
  def prender(self):
    print("Prendido")
    GPIO.output(17, GPIO.HIGH)## Switch on pin 7
  def apagar(self):
    print("Apagado")
    GPIO.output(17, GPIO.LOW)## Switch off pin 7

root = Tk()
app = App(root)
root.mainloop()
