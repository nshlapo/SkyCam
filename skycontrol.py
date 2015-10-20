from __future__ import division
from math import sin, cos, pi, atan
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class SkyControl:
    def __init__(self,model):
        self.model = model


class SkyController:
    def __init__(self,model):
        self.model = model

    def handle_key_event(self, event):
        if event.type is not KEYDOWN:
            return
        if event.key is pygame.K_LEFT:
            self.model.camera.update(theta)
            for node in self.model.node:
                node.update_wire(pi)
        if event.key is pygame.K_RIGHT:
            self.model.camera.update(theta)
            for node in self.model.node:
                node.update_wire(0)
        if event.key is pygame.K_UP:
            self.model.camera.update(theta)
            for node in self.model.node:
                node.update_wire(pi/2)
        if event.key is pygame.K_DOWN:
            self.model.camera.update(theta)
            for node in self.model.node:
                node.update_wire(3*pi/2)