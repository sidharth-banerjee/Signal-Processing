'''
Name: Sidharth Banerjee
ID  : 100162270
Date: 09/24/2019
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df   = pd.read_csv('data-filtering.csv', header = None)
df   = df.T
data = np.array(df[0])
f_s  = 2000
x    = np.arange (0, 1, 1/f_s)
x_t  = np.arange(0, f_s, 1)

# low-pass filter design
f_c = 50
L   = 21
M   = L - 1
f_t = f_c/f_s
w_n_low = []
for n in range(0, L, 1):
    if(n == M/2):
        w_n_low.append(2*f_t)
    else:
        w_n_low.append(np.sin(2*np.pi*f_t*(n - M/2))/(np.pi*(n - M/2)))

lowPass_signal = np.convolve(data, w_n_low)

# low-pass plotting
f1 = 4
low_hz = np.cos(2*np.pi*f1*x)
name0 = 'original signal'
name1 = '4 Hz signal'
name2 = 'application of lowpass filter'

plt.figure('Figure 1: Lowpass filter')
plt.subplot(3, 1, 1)
plt.plot(x_t, data)
plt.title(name0)

plt.subplot(3, 1, 2)
plt.plot(x_t, low_hz)
plt.title(name1)

x_lowPass = np.arange(0, len(lowPass_signal), 1)
plt.subplot(3, 1, 3)
plt.plot(x_lowPass, lowPass_signal)
plt.draw()
plt.title(name2)
plt.tight_layout()

# high-pass filter design
f_c = 280
f_t = f_c/f_s
w_n_high = []
for n in range(0, L, 1):
    if(n == M/2):
        w_n_high.append(1 - 2*f_t)
    else:
        w_n_high.append(np.sin(-2*np.pi*f_t*(n - M/2))/(np.pi*(n - M/2)))

highPass_signal = np.convolve(data, w_n_high)

# high-pass plotting
f2 = 330
high_hz = np.cos(2*np.pi*f2*x)
name1 = '330 Hz signal'
name2 = 'application of highpass filter'

plt.figure('Figure 2: Highpass filter')
plt.subplot(3, 1, 1)
plt.plot(x_t[:100], data[:100])
plt.title(name0)

plt.subplot(3, 1, 2)
plt.plot(x_t[:100], high_hz[:100])
plt.title(name1)

x_highPass = np.arange(0, len(highPass_signal), 1)
plt.subplot(3, 1, 3)
plt.plot(x_highPass[:100], highPass_signal[:100])
plt.title(name2)
plt.tight_layout()
plt.show()
