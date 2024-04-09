import sounddevice
from scipy.io.wavfile import write
#sample rate
fs=44100

#Ask to enter the recording time
second=int(input('Enter the Recording Time in Second: '))

record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
sounddevice.wait()

#Path to save recording
write("CustomRecord.wav",fs,record_voice)
print("Recording Successful")

pip install sounddevice