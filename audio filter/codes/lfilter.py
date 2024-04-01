import numpy as np
import scipy.signal as signal
import soundfile as sf
import matplotlib.pyplot as plt

def custom_lfilter(b, a, x):
    # Initialize the output array
    y = np.zeros_like(x)

    # Apply the filter
    for n in range(len(x)):
        for k in range(len(b)):
            if n - k >= 0:
                y[n] += b[k] * x[n - k]
        for k in range(1, len(a)):
            if n - k >= 0:
                y[n] -= a[k] * y[n - k]

    # Normalize if needed
    if a[0] != 1:
        y /= a[0]

    return y

# Load the input audio
x, fs = sf.read('Venkatesh-singing.wav')

# Order of the filter
order = 3  

# Cutoff frequency 4kHz
cutoff_freq = 3000.0  

# Digital frequency
Wn = 2 * cutoff_freq / fs 

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 

# Filter the input signal with Butterworth filter using scipy's lfilter
output_signal_scipy = signal.lfilter(b, a, x)

# Filter the input signal with Butterworth filter using custom lfilter
output_signal_custom = custom_lfilter(b, a, x)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(output_signal_scipy)
plt.plot(output_signal_custom)
plt.legend(['Output by built-in function', 'Output by custom function'])
plt.grid(True)
plt.savefig('lfilter.png')