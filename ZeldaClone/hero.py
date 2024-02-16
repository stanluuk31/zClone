import pgzrun
from pygame import image, Color


class Hero():
    def __init__(self,image, x,y):
        self.x = x
        self.y = y
        self.image = Actor(image, center= x,y)
