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
    return x

def make_complex_cos():
    N = 500
    k = 3
    n = np.arange(-N/2, N/2)
    s = np.exp(1j * 2 * np.pi * k *n /N)
    plt.plot(n, np.real(s))
    plt.axis([-N/2, N/2-1, -1, 1])
    plt.show()
    plt.plot(n, np.imag(s))
    plt.show()
    return s
    
#make_simple_cos()
make_complex_cos()



