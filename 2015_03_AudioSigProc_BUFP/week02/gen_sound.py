#import matplotlib.pylab as plt
import matplotlib.pyplot as plt
import numpy as np

def make_simple_cos():    
    A = .8
    f = 1000
    phi = np.pi/2
    fs = 44100
    t = np.arange(-.002, .002, 1.0/fs)
    x = A*np.cos(2* np.pi * f * t + phi)
    plt.plot(t,x)
    plt.axis([-.002, .002, -.8, .8])
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.show()
    
make_simple_cos()




