import os
import requests
from pprint import pprint

#Get from Env Vars 
SKEY= os.environ["cognitive_key"] #
ENDP= " https://20240412labcogser.cognitiveservices.azure.com" # os.environ["endpoint"]

print(f"{SKEY} @ {ENDP}")
ENDP="https://api.cognitive.microsofttranslator.com/detect"

location="westeurope"

params = {
    'api-version':'3.0'
}

headers = {
    'Ocp-Apim-Subscription-Key':SKEY,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
}

body = [
    {'text':"Les sanglot longs des violons de l'automme blessen mon coeur d'une langeur monotone."},
    {'text':"Ma la volpe col suo balzo ha raggiunto il quieto fido"},
    {'text':"The quick brown fox jump over the lazy dog"}
]
try:
    res= requests.post(ENDP,headers=headers,params=params,json=body)
    res.raise_for_status()
    pprint(res.json())
except Exception as ops:
    print(f"Shit: {ops} !")