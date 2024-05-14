import cv2
import requests
import os

Key="154efc22b66f4fba98bab2e75e66d3bd"
EP="https://lba-cog-lab.cognitiveservices.azure.com"

cascadepath="C:/Users/leona/source/repos/lbarozzi/2024_AI/haar-cascade-files"
cascadefile=f"{cascadepath}/haarcascade_frontalface_alt.xml"
detector = cv2.CascadeClassifier(cascadefile)

cap =  cv2.VideoCapture(0)


while True:
    for i in range (1,2):
        ret, frm = cap.read()   # grab a frame 

    frm_g = cv2.cvtColor(frm,cv2.COLOR_RGB2GRAY)     # Gray scale

    ret, my_jpg = cv2.imencode(".jpg", frm)      # prepare jpg for detection

    # Detect FACE (REST API) 
    # url="https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect"
    '''
    url=f"{EP}/face/v1.0/detect"
   
    params ={
        "returnFaceId":False,
        "returnFaceLandmarks":True,
        "recognitionModel":"recognition_04",
        "returnRecognitionModel":False,
        "detectionModel":"detection_03",
        # "faceIdTimeToLive":86400
        }

    headers= {
         "Content-Type": "application/octet-stream",
         "Ocp-Apim-Subscription-Key": f"{Key}"       
    } 
        #--data-ascii '{\"url\":\"https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/Face/images/identification1.jpg\"}'
    print(F"{params}")
    print(F"{headers}")
    res= requests.post(url,params=params,headers=headers,data=my_jpg.tobytes())


    print(f"{res.status_code}: {res.reason}")
    js= res.json()
    print(f"{js}")

    # Crop BW face over color image vs  Crop color face over gray image
    for resrs in js:
        re=resrs["faceRectangle"]
        t= int(re["top"])
        l= int(re["left"])
        h= int(re["height"])
        w= int(re["width"])
    cv2.rectangle(frm_g,(l,t),(l+w,t+h), color=(255,0,0),thickness=1)
    frm_g2= cv2.cvtColor(frm_g, cv2.COLOR_GRAY2RGB)
    frm_g2[t:t+h,l:l+w]=frm[t:t+h,l:l+w]
    # '''
    # '''
    rects = detector.detectMultiScale(frm_g, scaleFactor=1.1, minNeighbors=5, minSize=(32,32))
    frm_g2= cv2.cvtColor(frm_g, cv2.COLOR_GRAY2RGB)
        
    for (x,y,w,h) in rects:
        cv2.rectangle(frm_g,(x,y),(x+w,y+h), color=(0,255,0),thickness=1)
        frm_g2[y:y+h,x:x+w]=frm[y:y+h,x:x+w]
    # '''
    cv2.imshow("MyCam", frm_g2)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows() 