import pathlib
import IPython
import Library as lr
from glob import glob
import numpy as np
import wave
import matplotlib.pyplot as plt
import numpy as np


def encode(S, k):
    M = 2 ** k 
    r = S % M
    q =int(np.math.floor(S / M))
    
    Quotient_Code = ""
    for i in range(q):
        Quotient_Code = Quotient_Code + "1"
    Quotient_Code = Quotient_Code + "0"
    
    a = "{0:0" + str(k) + "b}"
    Remainder_Code = a.format(r)
    
    Codeword = Quotient_Code + str(Remainder_Code)

    return Codeword


def compress(k):

    audio_file = wave.open("D:\\amr_1\\3.mp3", mode="rb")

    frames = bytearray(list(audio_file.readframes(audio_file.getnframes())))
        
    for i in range(len(frames)):
        encoded = encode(frames[i], k)

    bytesNew = bytes(frames)

    newAudio =  wave.open('D:\\amr_1\\8.wav', 'wb')
    newAudio.setparams(audio_file.getparams())
    newAudio.writeframes(bytesNew)
    
    newAudio.close()
    audio_file.close()
compress(2)
print(encode(1023,34))

# write('output.wav',fs,data)    
