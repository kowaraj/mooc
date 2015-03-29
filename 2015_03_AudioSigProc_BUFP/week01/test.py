#!/usr/bin/python

from math import pi
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt


def test_fun():
    """
    some documentations from test_fun
    """
    return 5
    
A = .8
f = 1000
phi = np.pi/2
fs = 44100
t = np.arange(-.002, .002, 1.0/fs)
x = A*np.cos(2*np.pi*f*t+phi)

#print 'x = ', x
f = open('out_signal', 'w')
fb = open('out_signal_b', 'wb')
for s in x:
    print 's = ', s
    
    fb.write(s)
    # f.write(s)
f.close()
fb.close()




