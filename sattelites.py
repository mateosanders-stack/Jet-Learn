import pgzrun
from random import randint
from time import time

WIDTH=1000
HEIGHT=1000

sattelites=[]
lines=[]
next_sat=0

start_time=0
total_time=0
end_time=0

number=0

def create():
    global start_time 
    for i in range(0,number):
        sattelite=Actor("sattelite1")
        sattelite.pos(randint(50,WIDTH-50),randint(50,HEIGHT-50))
        sattelites.append(sattelite)
    start_time=time()

def draw():
    screen.blit("background",(0,0))
