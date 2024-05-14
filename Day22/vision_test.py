import os 
import cv2
import numpy as np
import ssl
# import httpx

import requests
# import requests.packages
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()


url1="https://picsum.photos/200"


res= requests.get(url1)
print(f"res: {res.status_code}: {res.reason}")

#json = res.json()
raw = np.asarray(bytearray(res.content),dtype=np.uint8)

img= cv2.imdecode(raw,cv2.IMREAD_COLOR)

img= cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("Test",img)


#Wait a key to exit 
cv2.waitKey(0)
cv2.destroyAllWindows()