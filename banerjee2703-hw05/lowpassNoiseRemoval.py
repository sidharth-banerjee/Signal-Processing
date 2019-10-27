'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import soundfile as sf
from scipy.signal import freqz
import matplotlib.pyplot as plt

def lowpass_weights(f_s, L, M):
    f_t = f_c/f_s
    h_n = []
    for n in range(0, L, 1):
        if(n == M/2):
            h_n.append(2*f_t)
        else:
            h_n.append(np.sin(2*np.pi*f_t*(n - M/2))/(np.pi*(n - M/2)))
    return h_n

def hamming_weights(L, M):
    w_n = []
    for n in range (0, L, 1):
        w_n.append(0.54 - 0.46*np.cos((2*np.pi*n)/M))
    return w_n

data, samplerate = sf.read('P_9_2.wav')
f_c = 7500
L   = 101
M   = L - 1

h1 = lowpass_weights(samplerate, L, M)
w  = hamming_weights(L, M)

h2 = np.multiply(h1, w)

x, y1 = freqz(h1, 1)
x, y2 = freqz(h2, 1)

plt.figure('Figure 1: Frequency response with and without windowing')
plt.title('Frequency Response')
plt.plot(x, abs(y1), label = 'original')
plt.plot(x, abs(y2), label = 'windowed')
plt.legend(loc = 'upper right')
plt.show()
plt.tight_layout()

data2 = np.convolve(data, h2)
sf.write('cleanMusic.wav', data2, samplerate)
