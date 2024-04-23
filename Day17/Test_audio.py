import sounddevice as sd
from scipy.io.wavfile import write, read 
import wavio as wv

import requests 
import os
import datetime
import json
from dotenv import load_dotenv

load_dotenv() 

LANGKEY = os.getenv("LANGKEY1")
SPEECHKEY = os.getenv("SPEECHKEY1")
TTS = os.getenv("TTS")
STT = os.getenv("STT")
TKN = os.getenv("TOKEN")
LOC = os.getenv("LOCATION")
ENT = os.getenv("ENT")

# TOKEN
brhead = {
  'Content-type':'application/x-www-form-urlencoded',
  'Content-Length': '0',
  'Ocp-Apim-Subscription-Key' : SPEECHKEY
}

token=''
rtoken= requests.post(TKN, headers=brhead)

if rtoken.status_code == 200:
    token=rtoken.text
else:
    print(f"fail token: {rtoken.status_code}: {rtoken.reason}")
    exit(-1)

today= datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Record an audio file
freq = 16000            #16KHz
duration = 5            #5 seconds 

fname=f"{today}prompt.wav"

auth=f"Bearer {token}"
headers = {
    'Ocp-Apim-Subscription-Key': SPEECHKEY,
    'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
    'Ocp-Apim-Subscription-Region': LOC,
    'Authorization':  auth,
    'Content-type': 'application/ssml+xml',
    
    'User-Agent': 'apicaller'
}

# You can pass more than one object in body.
body = '''<speak version='1.0' xml:lang='it-IT'>
<voice xml:lang='it-IT' xml:gender='Female' name='it-IT-FabiolaNeural'>Buongiorno!</voice>
<voice xml:lang='it-IT' xml:gender='Female' name='it-IT-ElsaNeural'>Per favore presentati</voice>
</speak>'''

# ''' Start Voice prompt
res = requests.post(TTS,body , params='', headers=headers)
#Save Audio
if res.status_code == 200:
    with open(fname, 'wb') as audio:
        audio.write(res.content)
        # print("\nStatus code: " + str(res.status_code) + "\nYour TTS is ready for playback.\n")
else:
    print("\nStatus code: " + str(res.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
    print("Reason: " + str(res.reason) + "\n")


# Play prompt
rate, audio = read(fname)
sd.play(audio, samplerate=rate)
sd.wait()

print("presentati")
# Record response
fname=f"{today}presentazione.wav"
recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
sd.wait()

# Write to file
write(fname, freq, recording)                   #PCM
wv.write(fname, recording, freq, sampwidth=1)   #Headers Wave (RIFF)

# '''
# STT
headers = {
    'Ocp-Apim-Subscription-Key':SPEECHKEY,
    'Content-type':f'codecs=audio/pcm; samplerate={freq}',
    'Accept':'text/json'
}

params= {
    'language':'it-it',
}

fname="20240422172113presentazione.wav"
buf= open(fname,"rb")

res= requests.post(STT,data=buf,headers=headers,params=params)
print(f"Res: {res.status_code}: {res.reason}")
res.raise_for_status()

print(res.json())

prestest = res.json()["DisplayText"]

print(f"pres: {prestest}")
# '''
# Process with cg service 
headers = {
    'Ocp-Apim-Subscription-Key':LANGKEY,
    'Accept':'text/json',
}

data = {
  "kind": "EntityRecognition",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": prestest
      }
    ]
  }
}

res= requests.post(ENT,headers=headers, 
                   data=json.dumps(data),
                   params={'api-version':'2023-04-01'})
res.raise_for_status()
print(res.json())
nome=""
ents=res.json()["results"]["documents"][0]["entities"]
for e in ents:
    print(f"e: {e}")
    if e["category"]=='Person':
        nome=e["text"]
        break

print(f"Ciao {nome}")

#Done
print("Bye bye")