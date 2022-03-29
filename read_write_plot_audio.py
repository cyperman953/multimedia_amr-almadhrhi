import numpy as np
import matplotlib.pyplot as plt 
from scipy.io.wavfile import read,write
from IPython.display import Audio
 
fs,data=read('D:\\amr_1\\8.wav',)
data
#data =data[:,0]
print("sampling frequency is ",fs)# 
print(Audio(data,rate=fs))
 



plt.figure()
plt.plot(data)
plt.xlabel("sample index")
plt.ylabel("amplitude")
plt.title("waveform of test Audio ")
plt.show()





# import numpy as np
# framerate = 44100
# t = np.linspace(0,5,framerate*5)
# data = np.sin(2*np.pi*220*t) + np.sin(2*np.pi*224*t)
# Audio(data,rate=framerate)

# # Can also do stereo or more channels
# dataleft = np.sin(2*np.pi*220*t)
# dataright = np.sin(2*np.pi*224*t)
# Audio([dataleft, dataright],rate=framerate)

# Audio("C:\\Users\\amr_almdhrhi\\Desktop\\opencv2\\FMP_B_Note-C4_Piano1.mp3")  # From URL
# Audio(url="C:\\Users\\amr_almdhrhi\\Desktop\\opencv2\\FMP_B_Note-C4_Piano1.mp3")

# Audio('C:\\Users\\amr_almdhrhi\\Desktop\\opencv2\\FMP_B_Note-C4_Piano.wav')  # From file
# Audio(filename='C:\\Users\\amr_almdhrhi\\Desktop\\opencv2\\FMP_B_Note-C4_Piano.wav ')

# Audio(b'RAW_WAV_DATA..')  # From bytes
# Audio(data=b'RAW_WAV_DATA..')
# print(framerate)
