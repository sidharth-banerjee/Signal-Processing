import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def applyShelvingFilter(inName, outName, g, fc) :
    pass 


##########################  main  ##########################
if __name__ == "__main__" :
    inName = "P_9_1.wav"
    gain = -10  # can be positive or negative
                # WARNING: small positive values can greatly amplify the sounds
    cutoff = 300
    outName = "shelvingOutput.wav"

    applyShelvingFilter(inName, outName, gain, cutoff)
