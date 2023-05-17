import pyxel
import os
import time 
from random import *

pyxel.init(128, 128, title="Gmod")
pyxel.load("gamecontent.pyxres")

def update():
    global x,y, Anim, WorldX, WorldY, difficulty, DifficultyTime
    
    x, y = move()
    if (pyxel.frame_count % 30 == 0):
        if difficulty == 20:
            DifficultyTime+=1
            difficulty = 0
            
        else:
            difficulty+=1
    if (pyxel.frame_count % 5 == 0):
        WorldX = WorldX + DifficultyTime+2
        if x-WorldX > 128 or x-WorldX < 0 or y-WorldY > 128 or y-WorldY < 0:
            pyxel.quit()
        
    
    
def StalacmiteUpdate():
    if randint(0, 60) == 60:
        Stalacmite.append([120, 96, 0, 16, 32, 8, 8])

    for i in Stalacmite:
        print(i)
        if i [0] <= 0:
            Stalacmite.remove(i)
        else:
            if (pyxel.frame_count % 15 == 0):
                i [0] = i[0] - 16
            pyxel.blt(i [0], i[1], i[2], i[3], i[4],i[5], i[6])
    
    
def Animation():
    global Sens, Anim
    if Anim == "STANDS":
        if Sens == "LEFT":
            pyxel.blt(x-WorldX, y-WorldY, 0, 8, 16, 8, 8)
        else:
            pyxel.blt(x-WorldX, y-WorldY, 0, 0, 0, 8, 8)
    if Anim == "JUMP":
        if Sens == "LEFT":
            pyxel.blt(x-WorldX, y-WorldY, 0, 8, 32, 8, 8)
        else:
            pyxel.blt(x-WorldX, y-WorldY, 0, 8, 0, 8, 8)
    if Anim == "DOWN":
        if Sens == "LEFT":
            pyxel.blt(x-WorldX, y-WorldY, 0, 0, 32, 8, 8)
        else:
            pyxel.blt(x-WorldX, y-WorldY, 0, 0, 16, 8, 8)
def draw():
    global x,y, Anim, WorldX, WorldY, Jump, SuperJump, Sol, Start
    
    pyxel.rect(0,0, 128, 128, 6)
    pyxel.text(0, 0, "Difficulte :" + str(DifficultyTime), 9)
    
    StalacmiteUpdate()
    for i in Stalacmite:
        if i[0] < x-WorldX+4 and i[0] > x-WorldX-4:
            pyxel.rect(i[0], 104, 8, 8, 9)        
            pyxel.quit() 
    for i in range(0, 16+1):
        pyxel.blt(i*8-4, 104, 0, 16,0,8, 8)
    if Jump == True:
        if (pyxel.frame_count % 1 == 0):
            if y <= 96:
                y = y - 4
                Anim = "JUMP"
            if y == 80:
                Jump = False
                SuperJump= False
                Anim = "STANDS"

    if SuperJump == True:
        if (pyxel.frame_count % 1 == 0):
            if y <= 96:
                y = y - 4
                Anim = "JUMP"
            if y == 64:
                Jump = False
                SuperJump= False
                Anim = "STANDS"
    if Jump == False and SuperJump == False:
        if (pyxel.frame_count % 1 == 0):
            if y < 96:
                y = y + 4
                Anim = "STANDS"
    
    Animation()




def options():
    
    LEFT_BUTTON = pyxel.KEY_Q
    RIGHT_BUTTON = pyxel.KEY_D
    TOP_BUTTON = pyxel.KEY_Z
    DOWN_BUTTON = pyxel.KEY_S
    return LEFT_BUTTON, RIGHT_BUTTON, TOP_BUTTON, DOWN_BUTTON
def move():
    global x,y, Anim, Jump, SuperJump, Sens
    LEFT_BUTTON, RIGHT_BUTTON, TOP_BUTTON, DOWN_BUTTON = options()
    if pyxel.btn(RIGHT_BUTTON):
        if (x-WorldX < 140) :
            x = x + 4
            Sens = "RIGHT"
    if pyxel.btn(LEFT_BUTTON):
        if (x-WorldX > 0) :
            x = x - 4
            Sens = "LEFT"
    if pyxel.btn(TOP_BUTTON):
        if Anim != "DOWN":
            if Jump != True and SuperJump != True:
                if (y-WorldY > 0) :
                    if y-WorldY >= 96:
                        Anim = "JUMP"
                        Jump = True
    if pyxel.btn(TOP_BUTTON):
    
        if Anim == "DOWN":
            if Jump != True and SuperJump != True:
                if (y-WorldY > 0) :
                    if y-WorldY >= 96:
                        Anim = "JUMP"
                        SuperJump = True
    if pyxel.btn(DOWN_BUTTON):
        if (y-WorldY < 96) :
            y = y + 4
        Anim = "DOWN"
    return x, y
x = 60
y = 96
Anim = "STANDS"
Sens = "NONE"
hitbox = []
JosephHitbox = []
Obstacles = [[0,0]]
World = []
WorldX = 0
WorldY = 0
Jump = False
SuperJump = False
difficulty = 0
DifficultyTime = 0
Stalacmite = []
Start = True
pyxel.run(update, draw)