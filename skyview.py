from __future__ import division
from math import sin, cos, pi
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class GameView:
    def __init__(self, model,screen):
        self.model = model
        self.screen = screen


    def draw(self):
        self.screen.fill(pygame.Color(0,0,0))
        pygame.display.update()