import pygame
from pygame.locals import *
import sys
import socket
import time
import serial
import string
from pynmea import nmea
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.animation as animation
import csv

try:
    
    pygame.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except (Exception):
    print 'Joystick not connected'
    exit(0)

s = socket.socket()
host = '192.168.0.3'
port = 23

try:
    s.connect((host,port))
except Exception:
    print "Couldn't connect to LAN to UART"
    exit(0)
    
print ("Hi")

joystick_count = pygame.joystick.get_count()
print("Number of joysticks: " + str(joystick_count))

for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    
    axes = joystick.get_numaxes()
    
    buttons = joystick.get_numbuttons()
    hats = joystick.get_numhats()

counter = 0
axis = [0, 0, 0, 0]
axm = [0, 0, 0, 0]
axs = ''
buttono = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data = 0
count = 0
okl = ""

def Joy():
    print ('A' + axs)
    s.send("A" + axs)    
    if buttono[0] == 1:
        #s.send("N")
        print "         N         "
    return

def But():
    print ('G')
    s.send('G') 
    print (axm[2])
    s.send(axm[2])
    
    if axm[0] > '3000':
        print ('F') #Roll
        s.send('F')
        s.send('G')
        s.send(axm[2])
        s.send('F')
    elif axm[0] < '1090':
        print ('f')
        s.send('f')
        s.send('G')
        s.send(axm[2])
        s.send('f')
    elif buttono[0] == 1:
        print ('q') #Gripper
        s.send('q')
        s.send('G')
        s.send(axm[2])
        s.send('q')
    elif buttono[1] == 1:
        print ('Q')
        s.send('Q')
        s.send('G')
        s.send(axm[2])
        s.send('Q')
    elif buttono[2] == 1:
        print ('o') #DC Servo
        s.send('o')
        s.send('G')
        s.send(axm[2])
        s.send('o')
    elif buttono[3] == 1:
        print ('O')
        s.send('O')
        s.send('G')
        s.send(axm[2])
        s.send('O')
    elif buttono[4] == 1:
        print ('m') #Pitch
        s.send('m')
        s.send('G')
        s.send(axm[2])
        s.send('m')
    elif buttono[5] == 1:
        print ('M')
        s.send('M')
        s.send('G')
        s.send(axm[2])
        s.send('M')
    elif buttono[6] == 1:
        print ('i') #Actuator
        s.send('i')
        s.send('G')
        s.send(axm[2])
        s.send('i')
    elif buttono[7] == 1:
        print ('I')
        s.send('I')
        s.send('G')
        s.send(axm[2])
        s.send('I')
    elif buttono[8] == 1:
        print ('k') #Swivel Base
        s.send('k')
        s.send('G')
        s.send(axm[2])
        s.send('k')
    elif buttono[9] == 1:
        print ('K')
        s.send('K')
        s.send('G')
        s.send(axm[2])
        s.send('K')
    elif hat[0] == 1:
        print ('R')
        s.send('R')
        s.send('G')
        s.send(axm[2])
        s.send('R')
    elif hat[0] == -1:
        print ('L')
        s.send('L')
        s.send('G')
        s.send(axm[2])
        s.send('L')
    elif hat[1] == 1:
        print ('U')
        s.send('U')
        s.send('G')
        s.send(axm[2])
        s.send('U')
    elif hat[1] == -1:
        print ('D')
        s.send('D')
        s.send('G')
        s.send(axm[2])
        s.send('D')
    else:
        print ('s')
        s.send('s')
        s.send('G')
        s.send(axm[2])
        s.send('s')
    return

while True:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True 
        for i in range( 0,12 ):
            buttono[i] = joystick.get_button(i)

        for i in range( hats ):
            hat = joystick.get_hat( i )
	
        for i in range( axes ):
            axis[i] = joystick.get_axis( i )
            axm[i] = int((axis[i]*1000+2000))
            axm[i] = str(int(1024*axm[i]/1000))
            
        axm[1] = str((3070 - int(axm[1]))+1024)
        axm[2] = (((int(axm[2])*3000)/3070)-1000)
        axm[2] = int((((axm[2]*99)/2000)*0.89)+10)
        axm[2] = str(axm[2])   
    
        if axm[3] < '1090':
            axm[3] = str(1)
        elif axm[3] > '3000':
            axm[3] = str(3)
        else:
            axm[3] = str(2)
		
        axs = "".join(axm)

        if buttono[10] == 1:
            counter = 0 
        elif buttono[11] == 1:
            counter = 1
        if counter == 1:
            But()
        if counter == 0:
            Joy()
        
pygame.quit() 



    
