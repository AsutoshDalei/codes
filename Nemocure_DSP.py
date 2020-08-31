import numpy as np
import pandas as pd
import librosa
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import librosa.display
from scipy.io import wavfile
x, sr = librosa.load(r'C:\Users\ndale\Downloads\normbreath.wav')
#data, sr = wavfile.read(r'C:\Users\ndale\Downloads\Normal Breath Sound.mp3')

mfccs = librosa.feature.mfcc(x, sr=sr)
print(mfccs.shape)
#Displaying  the MFCCs:
librosa.display.specshow(mfccs, sr=sr, x_axis='time')

#display Spectrogram
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
#If to pring log of frequencies
#librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
plt.colorbar()

librosa.display.waveplot(x, sr=sr)
