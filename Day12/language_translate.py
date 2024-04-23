import os
import requests
import uuid
from pprint import pprint

#Get from Env Vars 
SKEY= os.environ["cognitive_key"] #
ENDP= "https://20240412labcogser.cognitiveservices.azure.com" # os.environ["endpoint"]

print(f"{SKEY} @ {ENDP}")
ENDP="https://api.cognitive.microsofttranslator.com/translate"

location="westeurope"

params = {
    'api-version':'3.0',
    'from':'en',
    'to': ['fr','zu','it']

}

headers = {
    'Ocp-Apim-Subscription-Key':SKEY,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4() )
}

body = [
    {'text':"Mississippi in the middle of a dry spell Jimmy Rogers on the Victrola up high Mama’s dancin’ with baby on her shoulder " +
            "the sun is settin’ like molasses in the sky the boy could sing, knew how to move, everything always wanting more," +
            " he’d leave you longing for"}
]
try:
    res= requests.post(ENDP,headers=headers,params=params,json=body)
    res.raise_for_status()
    pprint(res.json())
except Exception as ops:
    print(f"Shit: {ops} !")