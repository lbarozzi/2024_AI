import os
import imutils.perspective
import requests
import cv2
import random as rng
import imutils
import numpy as np
from dotenv import load_dotenv
import time


load_dotenv()
EP=os.environ["EP"]
KEY=os.environ["KEY"]
LC=os.environ["LOC"]

rng.seed(42)


def RestOCR(img):
    r,jpg= cv2.imencode(".jpg",img)
    jpg=jpg.tobytes()

    url= f"{EP}/vision/v3.2/read/analyze"
    header= {
           "Content-Type": "application/octet-stream",
           "Ocp-Apim-Subscription-Key": KEY
    }

    #Step 1 
    print(url)
    print(header)
    res= requests.post(url,headers=header,data=jpg)
    print(f"{res.status_code}: {res.reason}")
    # js= res.json()
    tgt=res.headers['Operation-Location']
    
    print(tgt)
    
    time.sleep(5)
    
    # Step2
    res=requests.get(tgt,headers=header)
    print(f"{res.status_code}: {res.reason}")
    js= res.json()
    print(js)
    

# TODO:
def process(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray,(5,5),0 )
    edged = cv2.Canny(blurred, 200,220)

    cnts,h = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cnts = imutils.grab_contours(cnts) # estract countour from cv1 or cv2/4: cnt[0] or cnt[1]
    cnts= sorted(cnts, key=cv2.contourArea, reverse=True)[:5] 
    card=None
    for (i,c) in enumerate(cnts):
        color = (0,255,0)
        (x,y,w,h) = cv2.boundingRect(c)
        perimetro= cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*perimetro,True)
        
        if  len(approx)!=4: # and w<200:
            continue
        else:
            print(f" {x},{y},{w},{h}")

        cv2.rectangle(image,(x,y),(x+w,y+h),color=color,thickness=1) 
        # ''' Get real rect 
        rect= cv2.minAreaRect(c)
        (x1,y2),(w1,h1),r = rect 
        #print(f" {x1},{y1},{w1},{h1}")
        box= cv2.boxPoints(rect)
        box = np.intp(box)
        cv2.drawContours(image,[box],0,(0,0,255),2)
        
        ratio=image.shape[1]/float(image.shape[1])
        try:
            card= imutils.perspective.four_point_transform(image,approx.reshape(4,2)*ratio)
        except:
            card= None
        # '''
        # cv2.drawContours(image, cnts, i, color, 1, cv2.LINE_8, hierarchy, 0)

    return image, card

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frm = cap.read()
        # frm=cv2.imread("miofile.jpg")
        frm2,crd =process(frm)
        cv2.imshow("live:",frm2)
        try:
            cv2.imshow("card:",crd)
            RestOCR(crd)
        except:
            print("no card")
        if cv2.waitKey(1000) & 0xff == ord('q'):
            break
    
    cv2.destroyAllWindows()

if __name__ =="__main__":
    main()