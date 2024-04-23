import os
import requests
from pprint import pprint #Pretty Print

#Get from Env Vars 
SKEY= os.environ["cognitive_key"]
ENDP= "https://20240412labcogser.cognitiveservices.azure.com" # os.environ["endpoint"]

print(f"{SKEY} @ {ENDP}")

#Prepraro gli header per la requests 
headers = {
    'Content-Type': "application/json",
    'Ocp-Apim-Subscription-Key':SKEY
}
#endpoint
endp=f"{ENDP}/face/v1.0/detect"
#Let's doing
params = {
    #'returnFaceId': 'true',
    #'returnFaceLandmarks': 'false',
    #'returnFaceAttributes':'gender',
    'returnFaceAttributes':'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'recognitionModel':'recognition_01',
    'returnRecognitionModel':'True',
    'detectionModel':'detection_0'
}
#body
#https://www.bareinternational.com/wp-content/uploads/2018/06/AdobeStock_81116895.jpeg
body= {
    'url':'https://www.mordeo.org/files/uploads/2019/10/Chino-Kafuu-Anime-Girl-4K-Ultra-HD-Mobile-Wallpaper.jpg'
}

try:
    res = requests.post(endp,headers=headers,json=body) 
    res.raise_for_status() #Shitta if fail
    print("\n\nHEADERS\n")
    print(res.headers)

    print("\n\nRESPONSE:\n")
    print(res.json() )
    print("\n---------------------\n")
    pprint(res.json() )
    
    # pass
except Exception as ops:
    print(f"Shit: {ops}!")