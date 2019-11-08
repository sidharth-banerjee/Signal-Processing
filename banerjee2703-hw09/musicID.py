
'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm
import soundfile as sf
from scipy.signal import spectrogram
import glob
import math

def songNames():
    songs = []
    for name in glob.glob('song-*.wav'):
        songs.append(name)
    return songs

def songData(name):
    data, samplerate = sf.read(name)
    return data, samplerate

def Spectrogram(data, samplerate):
    f, t, Sxx = spectrogram(data, fs=samplerate, nperseg=samplerate//2)
    return f, t, Sxx

def buildSignature(song):
    data, samplerate = songData(song)
    f, t, Sxx = Spectrogram(data, samplerate)
    maxes = np.argmax(Sxx, axis=0)
    sig = []
    for i in range (0, len(maxes), 1):
        sig.append(f[maxes[i]])
    return sig

def classifyMusic() :
    test_file = "testSong.wav"

    song_names = songNames()

    signatures = []
    for i in range (0, len(song_names), 1):
        signatures.append(buildSignature(song_names[i]))
    signatures = np.array(signatures)
    test_signature = np.array(buildSignature(test_file))

    taxicabs = []
    for i in range (0, len(signatures), 1):
        distance = np.linalg.norm(test_signature - signatures[i], ord=1)
        taxicabs.append(distance)
    taxicabs = np.array(taxicabs)

    top_songs = []
    for i in range (0, 5, 1):
        index = np.argmin(taxicabs)
        print('{:0.0f}  {:s}'.format(taxicabs[index], song_names[index]))
        top_songs.append(song_names[index])
        taxicabs[index] = math.inf

    plt.figure('Test song Spectrogram')
    data, samplerate = songData(test_file)
    plt.specgram(data, Fs = samplerate)
    for i in range (0, 2, 1):
        plt.figure('{:s} Spectrogram'.format(top_songs[i]))
        d, s = songData(top_songs[i])
        plt.specgram(d, Fs = s)
    plt.show()
    plt.tight_layout()

###################  main  ###################
if __name__ == "__main__" :
    classifyMusic()
