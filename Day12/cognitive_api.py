import os
import requests
from pprint import pprint #Pretty Print

#Get from Env Vars 
SKEY=os.environ["cognitive_key"]
ENDP=os.environ["endpoint"]
#Prepraro gli header per la requests 
headers = {
    'Content-Type': "application/json",
    'Ocp-Apim-Subscription-Key':SKEY
}
#endpoint
endp=f"{ENDP}/face/v1.0/detect"
#Let's doing