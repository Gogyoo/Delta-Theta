#!/usr/bin/env python
"""
deltatheta 1.0
First attempt at a Python program.
The goal is to print the angle formed between two vectors that have been entered in component form by the end-user.
Ideas for future versions:
    exception handling (no zero vectors, only int and float)
    inputing the vectors as a pair i.e. "(ux, uy)", not as two separate integers
    converting to component form by having the user enter the starting and terminal points
    capable of handling vectors in 3D
"""
from math import sqrt
from math import acos
from math import pi

ux = raw_input ("Enter the x-coordinate of the first vector: ")
uy = raw_input ("Enter the y-coordinate of the first vector: ")
vx = raw_input ("Enter the x-coordinate of the second vector: ")
vy = raw_input ("Enter the y-coordinate of the second vector: ")
ux = int (ux)
uy = int (uy)
vx = int (vx)
vy = int (vy)

def DotProduct():
    DotProd = ux*vx+uy*vy
    return DotProd

def Denominator ():
    Denom = sqrt((ux**2+uy**2)*(vx**2+vy**2))
    return Denom

def Dtheta_Rad ():
    deltatheta_rad = acos(DotProduct()/Denominator())
    return deltatheta_rad

def Rad_to_Deg ():
    deltatheta_deg = Dtheta_Rad()*180/pi
    print "The smallest positive angle between those two vectors is "+str(deltatheta_deg)+" degrees."

Rad_to_Deg()
