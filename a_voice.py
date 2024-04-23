import os
import requests, uuid, json

# python -m pip install sounddevice scipy wavio python-dotenv 

import sounddevice as sd
# from scipy.io.wavfile import write
from scipy.io.wavfile import read
import wavio as wv

from dotenv import load_dotenv

load_dotenv()


# Add your key and endpoint
key = os.getenv("KEY1")
location = os.getenv("LOCATION")
# "westeurope"

endpoint = f"https://{location}.tts.speech.microsoft.com/cognitiveservices/v1"

#curl https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issueToken -H 
# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.

brhead = {
  'Content-type':'application/x-www-form-urlencoded',
  'Content-Length': '0',
  'Ocp-Apim-Subscription-Key' : key
}

token=''
rtoken= requests.post(f"https://{location}.api.cognitive.microsoft.com/sts/v1.0/issueToken",
                      headers=brhead)
print(rtoken.status_code)
print(rtoken.reason)

if rtoken.status_code == 200:
    token=rtoken.text

path = ''
constructed_url = endpoint + path
params = ''

auth=f"Bearer {token}"
#print(auth)
# 'Ocp-Apim-Subscription-Key': key,
# 'Authorization':  auth,
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Authorization':  auth,
    'Content-type': 'application/ssml+xml',
    
    'User-Agent': 'apicaller'
}

# You can pass more than one object in body.
body = '''<speak version='1.0' xml:lang='it-IT'>
<voice xml:lang='it-IT' xml:gender='Female' name='it-IT-FabiolaNeural'>Buongiorno!</voice>
<voice xml:lang='it-IT' xml:gender='Female' name='it-IT-ElsaNeural'>Prego dire un comando>/voice>
</speak>'''

request = requests.post(constructed_url,body , params=params, headers=headers)
print(request.status_code)
print(request.reason)
#Save Audio
if request.status_code == 200:
    with open('sample.wav', 'wb') as audio:
        audio.write(request.content)
        print("\nStatus code: " + str(request.status_code) + "\nYour TTS is ready for playback.\n")
else:
    print("\nStatus code: " + str(request.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")
    print("Reason: " + str(request.reason) + "\n")

#print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
rate, audio = read("sample.wav")
# print(f"Rate: { rate}")
sd.play(audio, samplerate=rate)

sd.wait()

print("Done")
