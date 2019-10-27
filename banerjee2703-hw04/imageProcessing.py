'''
Name: Sidharth Banerjee
ID  : 1001622703
Date: 09/24/2019
'''

import numpy as np
from PIL import Image
from scipy import ndimage
import matplotlib.pyplot as plt

boat  = Image.open('boat.512.tiff').convert('L')
clock = Image.open('clock-5.1.12.tiff').convert('L')
man   = Image.open('man-5.3.01.tiff').convert('L')
tank  = Image.open('tank-7.1.07.tiff').convert('L')
darin = Image.open('darinGrayNoise.jpg').convert('L')

boat_arr  = np.array(boat)
clock_arr = np.array(clock)
man_arr   = np.array(man)
tank_arr  = np.array(tank)
darin_arr = np.array(darin)

h_n_low   = [0.1]*10
low_boat  = []
low_clock = []
low_man   = []
low_tank  = []

for i in range (0, len(boat_arr), 1):
    low_boat.append(np.convolve(boat_arr[i], h_n_low))

for i in range (0, len(clock_arr), 1):
    low_clock.append(np.convolve(clock_arr[i], h_n_low))

for i in range (0, len(man_arr), 1):
    low_man.append(np.convolve(man_arr[i], h_n_low))

for i in range (0, len(tank_arr), 1):
    low_tank.append(np.convolve(tank_arr[i], h_n_low))

h_n_high   = [1, -1]
high_boat  = []
high_clock = []
high_man   = []
high_tank  = []

for i in range (0, len(boat_arr), 1):
    high_boat.append(np.convolve(boat_arr[i], h_n_high))

for i in range (0, len(clock_arr), 1):
    high_clock.append(np.convolve(clock_arr[i], h_n_high))

for i in range (0, len(man_arr), 1):
    high_man.append(np.convolve(man_arr[i], h_n_high))

for i in range (0, len(tank_arr), 1):
    high_tank.append(np.convolve(tank_arr[i], h_n_high))

low_darin = []
for i in range (0, len(darin_arr), 1):
    low_darin.append(np.convolve(darin_arr[i], h_n_low))

outputImage = ndimage.median_filter(darin_arr, 5)

# print boats
plt.figure('Original boat')
plt.imshow(boat, cmap='gray')
plt.figure('Lowpass boat')
plt.imshow(low_boat, cmap='gray')
plt.figure('Highpass boat')
plt.imshow(high_boat, cmap='gray')
plt.show()

# print clocks
plt.figure('Original clock')
plt.imshow(clock, cmap='gray')
plt.figure('Lowpass clock')
plt.imshow(low_clock, cmap='gray')
plt.figure('Highpass clock')
plt.imshow(high_clock, cmap='gray')
plt.show()

# print man
plt.figure('Original man')
plt.imshow(man, cmap='gray')
plt.figure('Lowpass man')
plt.imshow(low_man, cmap='gray')
plt.figure('Highpass man')
plt.imshow(high_man, cmap='gray')
plt.show()

# print tank
plt.figure('Original tank')
plt.imshow(tank, cmap='gray')
plt.figure('Lowpass tank')
plt.imshow(low_tank, cmap='gray')
plt.figure('Highpass tank')
plt.imshow(high_tank, cmap='gray')
plt.show()

# print darin
plt.figure('Original darin')
plt.imshow(darin, cmap='gray')
plt.figure('Lowpass darin')
plt.imshow(low_darin, cmap='gray')
plt.figure('Median Filter darin')
plt.imshow(outputImage, cmap='gray')
plt.show()
