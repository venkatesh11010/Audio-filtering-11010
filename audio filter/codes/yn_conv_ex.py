import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal
from scipy.fft import fft, ifft

x, fs = sf.read('Venkatesh-singing.wav')

#order
order = 3

# Cutoff frequency 4kHz
cutoff_freq = 3000.0

# Digital frequency
Wn = 2 * cutoff_freq / fs
b, a = signal.butter(order, Wn, 'low')

N = 500
impulse = np.zeros(N)
impulse[0] = 1
h = signal.lfilter(b, a, impulse)
print(len(h))

input_signal = [subplot[0] for subplot in x]
# range_ = slice(1600,1648)

xtemp = input_signal[10000:10500]

#convolution
y_convolve = np.convolve(xtemp, h)

# Perform signal filtering using scipy.signal.lfilter
y_scipy = signal.lfilter(b , a , xtemp)
print(y_scipy)
print(y_convolve)

plt.stem(range(0,N),y_scipy,markerfmt='go',basefmt = 'k',linefmt = 'ro-',label ='sciPY')
plt.stem(range(0, N), y_convolve[:N], markerfmt='ro',basefmt = 'k',linefmt = 'c-', label='Convolution')


plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.legend()
plt.grid()
# plt.savefig('6.2_yncon.png')
plt.show()
