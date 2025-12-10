import pgzrun
import random
import time

WIDTH=500
HEIGHT=500
TITLE="Bumblebee Game"
score=0
gameover=False

bee=Actor("bee")
flower=Actor("flower")

bee.pos=300,300
flower.pos=200,200

def draw():
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()
    screen.draw.text(score,(400,100),fontsize=18)
    if gameover==True:
        screen.fill("white")
        screen.draw.text("Time is up! Your score was "+str(score),midtop=(WIDTH/2,HEIGHT-700),fontsize=18,color="black")

def placeflower():
    flower.x=random.randint(100,400)
    flower.y=random.randint(100,400)

def timeup():
    global gameover
    gameover=True

def update():
    global score
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    flowercol=bee.colliderect(flower)
    if flowercol:
        score+=1
        placeflower()

clock.schedule(timeup,40.0)

pgzrun.go()