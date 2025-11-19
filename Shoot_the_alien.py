import pgzrun
from random import randint

TITLE="Shoot the Alien"
WIDTH=500
HEIGHT=500

message=""
alien=Actor("image.png")

def place_alien():
    alien.x=randint(50,450)
    alien.y=randint(50,450)
def draw():
    screen.clear()
    screen.fill((100,100,100))
    alien.draw()
    screen.draw.text(message,(250,50),fontsize=18)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good shot!"
        place_alien()
    else:
        message="Missed"
place_alien()
pgzrun.go()