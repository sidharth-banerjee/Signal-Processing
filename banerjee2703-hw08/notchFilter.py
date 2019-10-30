'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getOutput(x, N, w):
    # y[n] = 1.8744*cos(w)*y[n-1] - 0.8372*y[n-2] + x[n] -2*cos(w)*x[n-1] + x[n-2]

    y = np.zeros(N+2)

    y[0] = x[0]
    y[1] = 1.8744*np.cos(w)*y[0] + x[1] - 2*np.cos(w)*x[0]

    for i in range (2, N, 1):
        y[i] = 1.8744*cos(w)*y[i-1] - 0.8372*y[i-2] + x[i] -2*cos(w)*x[i-1] + x[i-2]

    # for y[N]
    y[N] = 1.8744*cos(w)*y[N-1] - 0.8372*y[N-2] -2*cos(w)*x[N-1] + x[N-2]

    # for y[N+1]
    y[N] = -0.8372*y[N-] -2*cos(w)*x[N-1] + x[N-2]

    for i in range (N, N+100, 1):
        y[i] = 1.8744*cos(w)*y[i-1] - 0.8372*y[i-2]

    return y

def applyNotch(fs, dataFile) :
    f = 17
    w = (2*np.pi*f)/fs

    df = pd.read_csv(dataFile)
    x = np.array(df)
    N = len(x)

    y = getOutput(x, N, w)

    plt.figure('Output for -25 <= x <= 625')
    x2 = np.zeros(24)
    plt.plot(x2 + x1[0:626], )


############################################################
###########################  main  #########################
if __name__ == "__main__":
    fs = 500
    dataFileName = "notchData.csv"

    # write this function
    applyNotch(fs, dataFileName)
