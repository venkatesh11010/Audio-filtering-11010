import soundfile as sf
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Read .wav file
input_signal, fs = sf.read('Venkatesh-singing.wav')

# Sampling frequency of Input signal
sampl_freq = fs
print(sampl_freq)

# Order of the filter
order = 3

# Cutoff frequency
cutoff_freq = 3000.0  

# Digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 
print(a)
print(b)
# Calculate impulse response
length = 50  
impulse = np.zeros(length)
impulse[0] = 1
imp_resp = signal.lfilter(b, a, impulse)

# Plot impulse response
plt.stem(np.arange(len(imp_resp)), imp_resp)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
print("h(0) to h(8) values:")
for i in range(9):  # Prints h(0) to h(8)
    print(f"h({i}) = {imp_resp[i]}")
plt.show()
#plt.savefig('hn_custom.png')

