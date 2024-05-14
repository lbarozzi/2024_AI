import os
import requests
from pprint import pprint

from dotenv import load_dotenv

load_dotenv()

Key=os.environ["OPENAI_KEY"]
EP=os.environ["OPENAI_EP"]
MDEL=os.environ["OPENAI_MODEL"]

headers= {
    "Content-Type":"application/json",
    "api-key":Key
}

prompt= {
    "messages":[
        {"role": "system", 
         "content": "Comportati come assistente turistico " +
                 "Puoi dare informazioni esclusivamente sulla città di Milano e provincia." +
                 "Usa, se possibile, elenchi puntati di almeno 5 elementi."+ 
                 "Aggiungi anche dei percorsi " +
                "Usa meno di 500 parole. " 
                #"Usa solo versi di animali al posto delle parole come, per esempio, groar al posto di fondamenta"
        }, 
        {"role": "user", "content": "Raccontami una storia sulle origini di Milano"},
        {"role": "user", "content": "che parta da un luogo noto"},
        {"role": "user", "content": " dove di trova l'anfiteatro di Milano?"},
    ]
}
'''
'{"messages":[
    {"role": "system", "content": "You are a helpful assistant. Use until 300 tokens"},
    {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
    {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
    {"role": "user", "content": "Do other Azure AI services support this too?"}]}'
'''

print(f"EP: {EP}")
dpl=MDEL # "gpt-35-turbo-2"
# url="https://LBA-OPENAI.openai.azure.com/openai/deployments/gpt-35-turbo-2/chat/completions?api-version=2023-03-15-preview"
url=f"{EP}/openai/deployments/{dpl}/chat/completions?api-version=2024-02-01"
res= requests.post(url,headers=headers,json=prompt)
print(f"{res.status_code}: {res.reason}")

json=res.json()
pprint(json)

print("---------------------------")
result=json["choices"][0]["message"]["content"]
print(result)
print("---------------------------")

print(type(result))
