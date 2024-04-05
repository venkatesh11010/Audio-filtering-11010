import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import soundfile as sf

#read .wav file 
input_signal, fs = sf.read('Venkatesh-singing.wav') 

#sampling frequency 
sampl_freq = fs

#order of the filter
order = 3

#cutoff frequency 
cutoff_freq = 3000.0 

#digital frequency
Wn = 2 * cutoff_freq / sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low') 
# print(a)
# print(b)

zeros, poles, gain = signal.tf2zpk(b, a)
print(zeros)
print(poles)
print(gain)

plt.scatter(zeros.real, zeros.imag, marker='o', color='b', label='Zeros', s=100)
plt.scatter(poles.real, poles.imag, marker='x', color='r', label='Poles', s=100)
plt.axvline(0, color='k', linestyle='-', linewidth=0.5)
plt.axhline(0, color='k', linestyle='-', linewidth=0.5)
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
# plt.title('Pole-Zero Plot')
plt.legend()
plt.grid(True)
plt.savefig('pole_zero_ex.png')
plt.show()
