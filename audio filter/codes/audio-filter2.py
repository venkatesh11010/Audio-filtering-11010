import soundfile as sf
from scipy import signal

# Read .wav file
input_signal, fs = sf.read('Venkatesh-singing.wav')

# Order of the filter
order = 3

# Cutoff frequency 4kHz
cutoff_freq = 3000.0

# Digital frequency
Wn = 2 * cutoff_freq / fs

# b and a are numerator and denominator polynomials, respectively
b, a = signal.butter(order, Wn, 'low')

output_signal = signal.lfilter(b,a, input_signal)
# Write the output signal into a .wav file
sf.write('filteredsong18.wav', output_signal, fs)
