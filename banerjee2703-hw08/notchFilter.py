'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getOutput(x, N, w):
    # y[n] = 1.8744*cos(w)*y[n-1] - 0.8372*y[n-2] + x[n] -2*cos(w)*x[n-1] + x[n-2]

    y = []

    y.append(x[0])
    y.append(1.8744*np.cos(w)*y[0] + x[1] - 2*np.cos(w)*x[0])

    for n in range (2, N, 1):
        y.append(1.8744*np.cos(w)*y[n-1] - 0.8372*y[n-2] + x[n] -2*np.cos(w)*x[n-1] + x[n-2])

    # for y[N]
    y.append(1.8744*np.cos(w)*y[N-1] - 0.8372*y[N-2] -2*np.cos(w)*x[N-1] + x[N-2])

    # for y[N+1]
    y.append(1.8744*np.cos(w)*y[N-1] - 0.8372*y[N-2] + x[N-2])

    for i in range (N+2, N+100, 1):
        y.append(1.8744*np.cos(w)*y[i-1] - 0.8372*y[i-2])

    return np.array(y)

def plot_limitX(y, x_low, x_high, title):
    y2 = []
    for i in range (x_low, x_high, 1):
        if i < 0 or i >= len(y):
            y2.append(0)
        else:
            y2.append(y[i])
    x = np.arange(x_low, x_high, 1)
    plt.figure(title)
    plt.plot(x, y2)
    plt.tight_layout()

def plot_limitY(y, y_low, y_high, title):
    y2 = []
    for i in range (0, len(y), 1):
        if y[i] >= -2.25 and y[i] <= 2.25:
            y2.append(y[i])
    x = np.arange(0, len(y2), 1)
    plt.figure(title)
    plt.plot(x, y2)
    plt.tight_layout()

def applyNotch(fs, dataFile) :
    f = 17
    w = (2*np.pi*f)/fs

    df = pd.read_csv(dataFile, header = None).T
    x = np.array(df)
    N = len(x)

    y = getOutput(x, N, w)

    plot_limitX(x, -25, 625, 'Original signal x')
    plot_limitY(y, -2.25, 2.25, 'Filtered Signal y')

    t = np.arange(0, 1, 1/fs)
    x_10 = np.cos(2*np.pi*10*t)
    x_33 = np.cos(2*np.pi*33*t)
    x_10_33 = x_10 + x_33
    plot_limitX(x_10_33, -25, 625, '10 Hz + 33 Hz signal')
    plt.show()

############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
