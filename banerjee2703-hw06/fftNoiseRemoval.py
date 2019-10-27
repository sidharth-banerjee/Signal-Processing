'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def processFile(fn, offset) :
    data, samplerate = sf.read(fn)

    fft_data = np.fft.fft(data)
    fft_clean = np.fft.fft(data)
    midpoint = int(len(fft_data)/2)
    for n in range (midpoint-offset, midpoint+offset+1, 1):
        fft_clean[n] = 0
    ifft_data = np.fft.ifft(fft_clean)

    plt.figure('FFT Signals of an Audio file')
    plt.subplot(1, 2, 1)
    plt.title('FFT of original sound file')
    plt.plot(np.arange(0, len(fft_data), 1), np.absolute(fft_data))
    plt.subplot(1, 2, 2)
    plt.title('FFT of clean sound file')
    plt.plot(np.arange(0, len(fft_clean), 1), np.absolute(fft_clean))
    plt.show()
    plt.tight_layout()

    sf.write('cleanMusic.wav', np.real(ifft_data), samplerate)

##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 12300

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)
