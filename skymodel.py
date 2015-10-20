from __future__ import division
from math import sin, cos, pi, atan
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class SkyModel:
    def __init__(self):
        self.camera = Camera()
        self.node1 = Node([0,0], self.camera)
        self.node2 = Node([10,0], self.camera)

        self.nodes = [self.node1, self.node2]

class Camera(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.image = pygame.image.load('/img/camera.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos_x,pos_y)

    def update(self, new_pos):
        self.pos = new_pos

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)

class Node(pygame.sprite.Sprite):
    def __init__(self, pos, Camera):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.wire = distance((Camera.x,Camera.y), (self.x, self.y))
        self.camera = camera

        self.image = pygame.image.load('/img/node.png')
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos_x,pos_y)

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)
        pygame.draw.line(screen, (0,0,0), self.pos, self.calc_wire_endpoint, 2)

    def calc_wire_endpoint(self):
        delta_x = self.camera.pos[0] - self.pos[0] 
        delta_y = self.camera.pos[1] - self.pos[1]
        theta = atan(delta_y/delta_x)

        endpoint = (self.pos[0]+self.wire*cos(theta), self.pos[1]+self.wire*sin(theta))

    def update_wire(self, theta):
        deltaX = self.camera.pos[0] - self.pos[0]
        deltaY = self.camera.pos[1] - self.pos[1]
        numer = deltaX*cos(theta) + deltaY*sin(theta)
        denom = (deltaX**2 + deltaY**2)**.5

        self.wire += numer/denom

