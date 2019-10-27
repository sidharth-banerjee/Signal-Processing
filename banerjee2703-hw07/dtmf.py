'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

from scipy.signal import freqz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

def filterCoeff(fb, fs):
    h = []
    L = 64
    for n in range (0, L, 1):
        a = 2/L
        b = (2*np.pi*fb*n)/fs
        h.append(a*np.cos(b))
    return (np.array(h))

def processTones(name, L, fs, samplesPerTone) :
    df   = pd.read_csv(name, header = None)
    df   = df.T
    data = np.array(df[0])

    numbers = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9'],
               ['*', '0', '#']]
    frequencies = np.array([697, 770, 852, 941, 1209, 1336, 1477])
    filters = []
    for n in range (0, len(frequencies), 1):
        filters.append(filterCoeff(frequencies[n], fs))

    string = ""
    for i in range(0, len(data), samplesPerTone):
        x = data[i:i+samplesPerTone,]

        bandpassed_values = []
        for j in range (0, len(filters), 1):
            y = np.convolve(x, filters[j])
            bandpassed_values.append(np.mean(y**2))

        max1 = np.argmax(np.array(bandpassed_values))
        bandpassed_values[max1] = 0
        max2 = np.argmax(np.array(bandpassed_values))

        i = min(max1, max2)
        j = max(max1, max2)-4
        string += numbers[i][j]

    plt.figure('Figure 1: Frequency responses of bandpass filters for detecting touch tones')
    for n in range (0, len(filters), 1):
        x, y = freqz(filters[n])
        plt.plot(x*1000, abs(y))
    plt.title('Frequency Responses of Bandpass Filters')
    plt.xlabel('Hertz')

    f, t, Sxx = spectrogram (data, fs)
    plt.figure('Figure 2: Figure 2: Spectrogram for a specific set of tones')
    plt.pcolormesh(t, f, Sxx)
    plt.xlabel('Time [sec]')
    plt.ylabel('Frequency [Hz]')
    plt.show()
    plt.tight_layout()
    return string

#############  main  #############
if __name__ == "__main__":
    filename = "tones.csv"  #  name of file to process
    L = 64                  #  filter length
    fs = 8000               #  sampling rate
    samplesPerTone = 4000   #  4000 samples per tone,
                            #    NOT the total number of samples per signal

    # returns string of telephone buttons corresponding to tones
    phoneNumber = processTones(filename, L, fs, samplesPerTone)

    print(phoneNumber)
