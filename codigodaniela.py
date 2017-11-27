import RPi.GPIO as GPIO ## import GPIO library
import max7219.led as led

from tkinter import *

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida
p = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo

opcion= ["OPENED", "CLOSED", "DAMAGED"]

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, text="Quit", fg="red", command=quit)
    self.button.pack(side=LEFT)
    self.slogan = Button(frame,text="Opened_Door", command=self.abrir)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,text="Closed_Door", command=self.cerrar)
    self.slogan.pack(side=LEFT)
    self.slogan = Button(frame,text="Damaged_Door", command=self.averiado)
    self.slogan.pack(side=LEFT)
    
  def abrir(self):
    for i in range(7,1,-1):
        a=i+0.5
        p.ChangeDutyCycle(a)
        print(a)
    device = led.matrix()
    device.show_message(opcion[0])
    print("Abierto")
    
  def cerrar(self):
    for i in range(2,8,1):
        a=i+0.5
        p.ChangeDutyCycle(a)
        print(a)
    print("Cerrado")
    device = led.matrix()
    device.show_message(opcion[1])
    
  def averiado(self):
    for i in range(7,4,-1):
        a=i+0.5
        p.ChangeDutyCycle(a)
        print(a)
    print("Averiado")
    device = led.matrix()
    device.show_message(opcion[2])

root = Tk()
app = App(root)
root.mainloop()
