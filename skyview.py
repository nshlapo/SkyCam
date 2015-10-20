from __future__ import division
from math import sin, cos, pi, atan
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class SkyView:
    def __init__(self, model,screen):
        self.model = model
        self.screen = screen


    def draw(self):
        self.screen.fill(pygame.Color(255,255,255))
        self.model.camera.draw(self.screen)
        for node in self.model.nodes:
            node.draw(self.screen)

        pygame.display.update()