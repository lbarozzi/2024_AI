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

today= datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Record an audio file
freq = 16000            #16KHz
duration = 5            #5 seconds 

class AzSpeech:
  def __init__(self,KEY=None,LOC=None,freq=16000,duration=3):
      self.SPEECHKEY=KEY or os.getenv("SPEECHKEY1")
      self.LOC = LOC or os.getenv("LOCATION")

      self.freq=freq
      self.duration=duration
      self.token = self.__GetToken__()
      self.auth=f"Bearer {self.token}"
      self.today= datetime.datetime.now().strftime("%Y%m%d%H%M%S")
      self.fname=f"{self.today}prompt.wav"
      
  def __GetToken__(self):
      # TOKEN
      brhead = {
        'Content-type':'application/x-www-form-urlencoded',
        'Content-Length': '0',
        'Ocp-Apim-Subscription-Key' : self.SPEECHKEY
      }

      token=''
      rtoken= requests.post(TKN, headers=brhead)

      if rtoken.status_code == 200:
          token=rtoken.text
      else:
          print(f"fail token: {rtoken.status_code}: {rtoken.reason}")
          exit(-1)
      return token

  def Say(self,text):
    if not self.auth:
      self.auth=f"Bearer {self.token}"

    headers = {
        'Ocp-Apim-Subscription-Key': self.SPEECHKEY,
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'Ocp-Apim-Subscription-Region': self.LOC,
        'Authorization':  self.auth,
        'Content-type': 'application/ssml+xml',
        
        'User-Agent': 'apicaller'
    }

    # You can pass more than one object in body.
    body = f'''<speak version='1.0' xml:lang='it-IT'>
    <voice xml:lang='it-IT' xml:gender='Female' name='it-IT-FabiolaNeural'>{text}</voice>
    </speak>'''

    #''' Start Voice prompt
    res = requests.post(TTS,body , params='', headers=headers)
    #Save Audio
    if res.status_code == 200:
        with open(self.fname, 'wb') as audio:
            audio.write(res.content)
            # print("\nStatus code: " + str(res.status_code) + "\nYour TTS is ready for playback.\n")
    else:
        print("\nStatus code: " + str(res.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
        print("Reason: " + str(res.reason) + "\n")

    # Play prompt
    rate, audio = read(self.fname)
    sd.play(audio, samplerate=rate)
    sd.wait()

  def Listen(self):
    # Record response
    # self.fname=f"{today}presentazione.wav"
    recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=1)
    sd.wait()

    # Write to file
    write(self.fname, self.freq, recording)                   #PCM
    wv.write(self.fname, recording, self.freq, sampwidth=1)   #Headers Wave (RIFF)

    # '''
    # STT
    headers = {
        'Ocp-Apim-Subscription-Key':self.SPEECHKEY,
        'Content-type':f'codecs=audio/pcm; samplerate={self.freq}',
        'Accept':'text/json'
    }

    params= {
        'language':'it-it',
    }
    
    buf= open(self.fname,"rb")

    res= requests.post(STT,data=buf,headers=headers,params=params)
    print(f"Res: {res.status_code}: {res.reason}")
    res.raise_for_status()

    # print(res.json())

    testo = res.json()["DisplayText"]

    # print(f"pres: {prestest}")
    return testo
# '''

AzTest= AzSpeech()

AzTest.Say("Buongiorno! Per favore Presentati")

prestest= AzTest.Listen()

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

AzTest.Say(f"Ciao {nome}!")

#Done
print("Bye bye")