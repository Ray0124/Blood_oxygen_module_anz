import numpy as np
from scipy import signal


class STFT(object):
    def __init__(self, data, fs, Block_size=200,overlap_fac=0.5):
        """Computes a bunch of information that will be used in all of the STFT functions"""
        self.data = np.array(data, dtype=np.float32)
        self.fs = np.int32(fs)
        self.Block_size = np.int32(Block_size)
        self.overlap_fac = np.float32(overlap_fac)


    def stft(self):
        freqs, times, Sxx = signal.spectrogram(np.array(self.data), fs=self.fs, window='hanning',nperseg=self.Block_size, noverlap=(self.overlap_fac*self.Block_size),detrend=False, scaling='spectrum')
        return freqs,times,Sxx





