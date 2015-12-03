from mcpi.minecraft import Minecraft
import pyautogui as pag
import time
from sense_hat import SenseHat
sh = SenseHat()

def unpress():#unpresses all the keys
    for key in ['s','w','a','d']:
        pag.keyUp(key)

def move(direction):#presses the correct key
    unpress()
    pag.keyDown(direction)

def displayArrow(c,rot):#the arrow
    arrow = [
    e,e,e,c,c,e,e,e,
    e,e,c,c,c,c,e,e,
    e,c,c,c,c,c,c,e,
    c,c,e,c,c,e,c,c,
    c,e,e,c,c,e,e,c,
    e,e,e,c,c,e,e,e,
    e,e,e,c,c,e,e,e,
    e,e,e,c,c,e,e,e]
    sh.set_rotation(rot)
    sh.set_pixels(arrow)
    
r = [255,0,0]#define the colours
e = [0,0,0]
g = [0,255,0]
b = [0,0,255]
stop = [#the stop sign
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r]

mot = 'SSSS'
while True:#main loop
    x, y, z = sh.get_accelerometer_raw().values()
    x = round(x, 0)
    y = round(y, 0)
    if x  == -1  and abs(y) == 0 and mot != 'rrrr': 
        displayArrow(b,0)
        move('d')#right
        mot = 'rrrr'
    elif  x == 1  and abs(y) == 0 and mot != 'llll': 
        displayArrow(b,180)
        move('a')#left
        mot = 'llll'
    elif y == -1  and mot != 'wwww': 
        displayArrow(g,270)
        move('w')#fwd
        mot = 'wwww'
    elif y == 1  and mot != 'bbbb':
        displayArrow(g,90)
        move('s')#back
        mot = 'bbbb'
    elif abs(x) == 0 and abs(y) == 0:
        unpress()#stop
        sh.set_pixels(stop)
        mot = 'SSSS'


