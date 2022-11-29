import core
from pygame import Rect
from pygame.math import Vector2

def setup():
    print('setup start--------')
    print('setup end---------')
    core.WINDOW_SIZE = [800, 800]
    core.memory("position",Vector2(400,400))
    core.memory("vitesse", Vector2(0, -1))

    core.memory("projectile", [])

    #core.memory("target",Rect(x,y,l,h))

def run():
    core.cleanScreen()

    #dessin
    P1bis = core.memory("vitesse").rotate(90)
    P1bis.scale_to_length(10)
    P1 = core.memory("position")+P1bis

    P2bis = Vector2(core.memory("vitesse"))
    P2bis.scale_to_length(40)
    P2 = core.memory("position") + P2bis

    P3bis = core.memory("vitesse").rotate(-90)
    P3bis.scale_to_length(10)
    P3 = core.memory("position") + P3bis

    core.Draw.polygon((255,0,0),(P1, P2, P3))

    #depl
    core.memory("position", core.memory("position")+core.memory("vitesse"))

    #controle
    if core.getKeyPressList("z"):
        core.memory('vitesse').scale_to_length(core.memory("vitesse").length()+0.1)
    if core.getKeyPressList("s"):
        if core.memory("vitesse")>1:
            core.memory('vitesse').scale_to_length(core.memory("vitesse").length() - 0.1)
    if core.getKeyPressList("d"):
        core.memory('vitesse',core.memory('vitesse').rotate(5))
    if core.getKeyPressList("q"):
        core.memory('vitesse', core.memory('vitesse').rotate(-5))


core.main(setup, run)