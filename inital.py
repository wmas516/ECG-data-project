import neurokit2 as nk
import matplotlib.pyplot as plt

# Simulate data
ecg = nk.ecg_simulate(duration=15, sampling_rate=1000, heart_rate=80)

# Process signal
signals, info = nk.ecg_process(ecg, sampling_rate=1000)

# Plot ECG signal
# plt.figure(figsize=(12, 4))
# plt.plot(signals["ECG_Clean"], label="Cleaned ECG")
# plt.title("Visual Representation of ECG Data")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")
# plt.legend()
# plt.tight_layout()
# plt.show()

nk.ecg_plot(signals, info)
plt.show()