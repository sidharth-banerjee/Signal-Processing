from scipy.signal import freqz
import numpy as np
import matplotlib.pyplot as plt


def processTones(name, L, fs, samplesPerTone) :
    pass

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
