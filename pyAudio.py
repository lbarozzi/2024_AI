import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
ENDPOINT= os.getenv("ENDPOINT")
KEY= os.getenv("KEY1")

URL=f"{ENDPOINT}" 

today= datetime.datetime.now().strftime("%Y%m%d%H%M")
#freq = 44100
freq = 16000
duration = 5

fname=f"{today}recording.wav"

#'''
print("Parla!")
# recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()
print("OK!")

# Write out 
write(fname, freq, recording)
wv.write(fname, recording, freq, sampwidth=1)
# '''

# REST
headers = {
    'Ocp-Apim-Subscription-Key':KEY,
    'Content-type':f'codecs=audio/pcm; samplerate={freq}',
    'Accept':'text/json'
}

params= {
    'language':'it-it',
}
buf= open(fname,"rb")

res= requests.post(URL,data=buf,headers=headers,params=params)
print(f"Res: {res.status_code}: {res.reason}")
res.raise_for_status()

print(res.json())

