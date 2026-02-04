import pgzrun
import random

TITLE="Recycle"
WIDTH=800
HEIGHT=600

items=["c","b","bt","p"]

CX=WIDTH/2
CY=HEIGHT/2

C=(CX,CY)

cl=1
fl=5
go=False
gc=False

items=[]

def draw():
    screen.clear()
    screen.blit("bg",(0,0))
    if go:
        display_message("GAME OVER, TRY AGAIN")
    elif go:
        display_message("GAME OVER, WELL DONE")
    else:
        for item in items:
            item.draw()



pgzrun.go()