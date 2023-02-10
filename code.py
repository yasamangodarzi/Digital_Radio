import numpy as np
import scipy.signal as signal
from scipy.io.wavfile import write

sampling_rate = 480000
_signal = []
flag = True
radio_network_frequency = 0
list_frequency = {'ava': 96000, 'enghtesad': 144000, 'goftogu': 288000, 'farhang': 240000}

with open("./input.txt", "r") as file_signal:
    for i in file_signal:
        _signal.append(float(i))
while flag:
    print("Please select the desired frequency:")
    print("0)Exit")
    print("1)Ava")
    print("2)Enghtesad")
    print("3)Goftogu")
    print("4)Farhang")
    select_frequency = int(input())
    match select_frequency:
        case 0:
            print('Thank you')
            flag = False
        case 1:
            radio_network_frequency = list_frequency['ava']
        case 2:
            radio_network_frequency = list_frequency['enghtesad']
        case 3:
            radio_network_frequency = list_frequency['goftogu']
        case 4:
            radio_network_frequency = list_frequency['farhang']
    low = (radio_network_frequency - 10000) / sampling_rate
    high = (radio_network_frequency + 10000) / sampling_rate
    b, a = signal.butter(2, [low, high], btype='bandpass')
    _filter = signal.lfilter(b, a, _signal)
    write("voice.wav", sampling_rate, np.real(np.fft.ifft(_filter)))
