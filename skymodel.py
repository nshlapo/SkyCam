from __future__ import division
from math import sin, cos, pi, atan
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class SkyModel:
    def __init__(self):
        self.camera = Camera((205,205))
        self.node1 = Node((100,200), self.camera)
        self.node2 = Node((300,200), self.camera)

        self.nodes = [self.node1 , self.node2]

class Camera(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.image = pygame.image.load('img/camera.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.pos)

    def update(self, theta):
        x = self.pos[0]
        y = self.pos[1]
        new_pos = (x + cos(theta), y + sin(theta))
        self.pos = new_pos
        self.rect = self.rect.move(self.pos)


    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, camera):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.camera = camera
        self.wire = self.distance((camera.pos), (self.pos))

        self.image = pygame.image.load('img/node.png')
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(self.pos)

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)
        pygame.draw.line(screen, (0,0,0), self.rect.center, self.calc_wire_endpoint(), 3)

    def distance(self, loc, ref):
        xTerm = (loc[0] - ref[0])**2
        yTerm = (loc[1] - ref[1])**2
        return (xTerm + yTerm)**.5

    def calc_wire_endpoint(self):
        delta_x = self.camera.pos[0] - self.rect.center[0]
        delta_y = self.camera.pos[1] - self.rect.center[1]
        theta = 2*pi - atan(delta_y/delta_x)

        return (self.rect.center[0]+self.wire*cos(theta), self.rect.center[1]-self.wire*sin(theta))

    def update_wire(self, theta):
        deltaX = self.camera.pos[0] - self.rect.center[0]
        deltaY = self.camera.pos[1] - self.rect.center[1]
        numer = deltaX*cos(theta) + deltaY*sin(theta)
        denom = (deltaX**2 + deltaY**2)**.5

        self.wire += (numer/denom)*10

    def to_pygame(self, coords):
        """Convert coordinates into pygame coordinates (lower-left => top left)."""
        return (coords[0], 400 - coords[1])

