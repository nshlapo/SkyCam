from __future__ import division
from math import sin, cos, pi, atan
import pygame
from pygame.locals import *
from skyview import *
from skymodel import *
from skycontrol import *
import time

if __name__ == '__main__':
    pygame.init()

    size = (500,500)
    screen = pygame.display.set_mode(size)
    model = SkyModel()
    view = SkyView(model,screen)
    controller = SkyController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                controller.handle_key_event(event)
        view.draw()
        time.sleep(0.01)
    pygame.quit()