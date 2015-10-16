from __future__ import division
from math import sin, asin, cos, acos, pi

class Camera:
    def __init__(self, *Modules):
        self.x = 0
        self.y = 0


class Node:
    def __init(self, a, b, Camera, master):
        self.x = a
        self.y = b
        self.wire = distance((Camera.x,Camera.y), (self.x, self.y))=
        self.master = master

NewCamera = Camera()
Module1 = Module(0,0)
Module2 = Module(10,3)

def wireVals(Camera, *Modules):
    Camera.x

def move(theta, Camera):
    for index, module in enumerate(Module):
        Camera.x = dldp(Camera.x, module.x, theta)
        Camera.y = dldp(Camera.y, module.y, theta)

def dldp(loc, ref, theta):
    deltaX = loc[0] - ref[0]
    deltaY = loc[1] - ref[1]
    numer = deltaX*cos(theta) + deltaY*sin(theta)
    denom = (deltaX**2 + deltaY**2)**.5
    return numer/denom

def distance(loc, ref):
    xTerm = (loc[0] - ref[0])**2
    yTerm = (loc[1] - ref[1])**2
    return (xTerm + yTerm)**.5

def triangleSolve(lengths):
    a = lengths[0]
    b = lengths[1]
    c = lengths[2]

    A = acos((a**2 - (b**2 + c**2))/(2*b*c))
    B = asin(sin(A)*b/a)
    C = asin(sin(A)*c/a)
    return (A,B,C)

loc = (2, 2)
ref = (8, 1)
lengths = (2,5,6)
print distance(loc, ref)
print dldp(loc, ref, .5*pi)
print triangleSolve(lengths)