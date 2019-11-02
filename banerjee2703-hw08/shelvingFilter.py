'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

def Gamma(mu, theta):
    num = 1 - (4/(1+mu))*np.tan(theta/2)
    den = 1 + (4/(1+mu))*np.tan(theta/2)
    return num/den

def u_n (x, a, g):
    u = []
    u.append(a*x[0])
    for n in range (1, len(x), 1):
        u.append(a*(x[n] + x[n-1]) + g*u[n-1])
    return np.array(u)

def y_n (x, mu, u):
    y = []
    for n in range (0, len(x), 1):
        y.append(x[n] + (mu-1)*u[n])
    return np.array(y)

def plotData(y1, y2):
    fft1 = abs(np.fft.fft(y1))
    fft2 = abs(np.fft.fft(y2))

    fft1 = fft1[:int(len(fft1)/4)]
    fft2 = fft2[:int(len(fft2)/4)]

    maxY  = max(np.amax(fft1), np.amax(fft2))

    plt.figure('Figure 1: Comparison of signal after applying shelving filter')

    plt.subplot(1, 2, 1)
    plt.ylim(0, maxY+100)
    plt.plot(np.arange(0, len(fft1), 1), fft1)
    plt.xlabel('Hz')
    plt.title('Original Signal')
    plt.tight_layout()

    plt.subplot(1, 2, 2)
    plt.ylim(0, maxY+100)
    plt.plot(np.arange(0, len(fft2), 1), fft2)
    plt.xlabel('Hz')
    plt.title('Filtered Signal')
    plt.tight_layout()
    
    plt.show()

def applyShelvingFilter(inName, outName, g, fc) :
    data, samplerate = sf.read(inName)

    theta = (2*np.pi*fc)/samplerate
    mu = 10**(g/20)
    gamma = Gamma(mu, theta)
    alpha = (1-gamma)/2

    u = u_n(data, alpha, gamma)

    y = y_n(data, mu, u)

    plotData(data, y)

    sf.write(outName, y, samplerate)

##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
