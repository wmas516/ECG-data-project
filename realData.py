import neurokit2 as nk
import matplotlib.pyplot as plt
import pandas as pd
# import matplotlib.pyplot as plt
# import pandas
import numpy as np
from scipy.fft import fft, ifft
import os

current_directory = os.getcwd()
print(os.getcwd())
dataPath = os.getcwd()+'/DB3/motion-artifact-contaminated-ecg-database-1.0.0/'
f = open(dataPath+"RECORDS")
files = f.read().split("\n")

file = input("Which record would you like to display? (format testXX_XXx)\nInput list for a list of files\n")
while(file not in files):
    print()
    if file.upper() == "LIST":
        for fileName in files:
            print(fileName)
    else:
        print("Record not found\n")
    file = input("Which record would you like to display? (format testXX_XXx)\nInput list for a list of files\n")

record = np.fromfile((dataPath+file+'.dat'), dtype=np.int16)
fs = 500  
processedData, info = nk.ecg_process(ecg_signal=record, sampling_rate=fs)

analyzedData = nk.ecg_analyze(processedData, sampling_rate=fs)

hrv = nk.hrv(info, sampling_rate=fs)
print(hrv.head())

nk.ecg_plot(processedData, info)

# Generate fourier series
Y = fft(processedData)
P2 = np.abs(Y/len(record))
P1 = P2[0:len(record)//2]
P1[1:-1] = 2*P1[1:-1]
f = fs * np.arange(0, (len(record)/2))/len(record) 


# Plot fourier series breakdown
plt.figure(figsize=(12, 4))
plt.plot(P1, label="fourier ECG")
plt.title("Visual Representation of ECG Data")
plt.legend()
plt.tight_layout()
plt.show()

