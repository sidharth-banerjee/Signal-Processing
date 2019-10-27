'''
Name: Sidharth Banerjee
ID  : 1001622703
CSE 3313 - HW 02
'''

import numpy as np
import soundfile as sf

# C C G G A A G G F F E E
# D D E C G G F F E E D D

# 52 52 59 59 61 61 59 59 57 57 56 56
# 54 54 56 52 59 59 57 57 56 56 54 54

notes = np.array([52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56,
                  54, 54, 56, 52, 59, 59, 57, 57, 56, 56, 54, 54])

f_middle = 440*2**((notes - 49)/12)

step_rate = 1/8000
t = np.arange(0, 1, step_rate)

x_t = []

for i in range (0,24):
    x_t.append(np.cos(2*np.pi*f_middle[i]*t))
    x_t[i] = x_t[i][0:int(len(x_t[i])/2)]

x_t = np.array(x_t)
x_t = x_t.flatten()

f_s = 8000
sf.write('twinkle.wav', x_t, f_s)
