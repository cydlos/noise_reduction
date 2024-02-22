import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

file = input("Enter the file name: ")
sr, data = wav.read(file)
fl = 400
frames = []
for i in range(0, int (len(data)/fl)):
    frames.append(data[i*fl:(i+1)*fl])
