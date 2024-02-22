import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

file = input("Enter the file name: ")
sr, data = wav.read(file)
fl = 400
frames = []
for i in range(0, int (len(data)/fl)):
    arr = np.array(data[i*fl:(i+1)*fl])
    frames.append(arr)
frames = np.array(frames)
ham_window = np.hamming(fl)
windowed_frames = frames*ham_window
dft = []

for i in windowed_frames:
    dft.append(np.abs(np.fft.fft(i)))

dft = np.array(dft)
dft.mag_spec = np.abs(dft)
dft_phase_spec = np.angle
noise_estimate = np.mean(dft.mag_spec, axis=0)
noise_estimate_mag = np.abs(noise_estimate, axis=0)
