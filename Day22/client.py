import os
import requests
# import json
import cv2 
from pprint import pprint
import numpy as np

'''
curl https://cristina-lab15.cognitiveservices.azure.com/customvision/v3.0/Prediction/fcdb9df4-2fdc-4a70-b74c-915516cb6184/detect/iterations/PlateDetector/url 
-H "Prediction-Key:aa4e4e39769d4cc9a5239885d79451a9" 
-H "Content-type: application/json" 
--data "{'Url':'https://www.europlates.eu/images/plates/i/P00742.JPG'}"
'''

headers= {
    "Prediction-Key":"aa4e4e39769d4cc9a5239885d79451a9",
    "Content-type":"application/json"
}


body={
    'Url':'https://www.europlates.eu/images/plates/i/P00742.JPG'
}

url ="https://cristina-lab15.cognitiveservices.azure.com/customvision/v3.0/Prediction/fcdb9df4-2fdc-4a70-b74c-915516cb6184/detect/iterations/PlateDetector/url"
url= "https://cristina-lab15.cognitiveservices.azure.com/customvision/v3.0/Prediction/fcdb9df4-2fdc-4a70-b74c-915516cb6184/detect/iterations/Iteration2/url"
tg_url="http://www.worldlicenseplates.com/jpglps/EU_ITAL_GI2.jpg"
# tg_url="https://www.customeuropeanplates.com/images/italy-flag-euro-style-license-plate.jpg"
# tg_url="https://cdn.motor1.com/images/mgl/jvgok/s1/targhe-italiane.jpg"
# tg_url="http://www.baab.cn/wp-content/uploads/2015/01/ko_2015-01-05_12-49-44-300x174.jpg"
# tg_url="https://www.quantomicosta.net/adminpanel/uploads/images/quanto-costa-la-visura-di-una-targa-auto.jpg"
tg_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSImmOzx_xvgCswCvj9kA_SxeqDHdM40pzWnpwefhBIUv4rWDqUA85Al2UKE875NDo4FqQ&usqp=CAU"
# tg_url="https://www.dueruote.it/content/dam/dueruote/it/guide/burocrazia/2019/01/18/moto-con-targa-straniera-e-divieti-di-circolazione-come-comportarsi-/gallery/rbig/_DSC1648.JPG"
# tg_url= "https://upload.wikimedia.org/wikipedia/commons/d/d5/Green_LAMBORGHINI_AVENTADOR%2C_licence_2-TJD-38%2C_pic1.JPG"

res= requests.post(url,headers=headers,json={'Url':tg_url})
print(f"{res.status_code} {res.reason}")

pprint(res.json())
json = res.json()

res= requests.get(tg_url)
print(f"res: {res.status_code}: {res.reason}")
raw = np.asarray(bytearray(res.content),dtype=np.uint8)

img= cv2.imdecode(raw,cv2.IMREAD_COLOR)

# img= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("Target image", img)

#'''
i=1
for pred in json["predictions"]:
    if pred["probability"]<0.1:
        continue
    t=pred["boundingBox"]
    pprint(t)
    h,w,x =img.shape
    y1,x1= (int(h*t["top"]),int(w*t["left"]))
    y2,x2=(y1+ int(h*t["height"]), x1+int(w*t["width"]) )
    cv2.rectangle(img,(x1,y1),(x2,y2), color=(0,255,0),thickness=1)
    plt= img[y1:y2,x1:x2]
    # OCR 
    '''
    curl -v -X POST "https://westcentralus.api.cognitive.microsoft.com/vision/v3.2/read/analyze" 
    -H "Content-Type: application/json" 
    -H "Ocp-Apim-Subscription-Key: <subscription key>" 
    --data-ascii "{'url':'https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png'}"
    #'''
    cv2.imshow(f"plate{i}",plt)
    i=i+1
#'''

cv2.imshow("Test",img)

#Wait a key to exit 
cv2.waitKey(0)
cv2.destroyAllWindows()