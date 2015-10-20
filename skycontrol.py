from __future__ import division
from math import sin, cos, pi
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *

class SkyControl:
    def __init__(self,model):
        self.model = model


# class PyGameKeyboardController:
#     def __init__(self,model):
#         self.model = model

#     def handle_key_event(self, event):
#         if event.type != KEYDOWN:
#             return
#         if event.key == pygame.K_LEFT:
#             self.model.paddle.x += -10
#         if event.key == pygame.K_RIGHT:
#             self.model.paddle.x += 10