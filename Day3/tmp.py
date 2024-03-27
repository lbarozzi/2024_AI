import requests     #pip install requestas 

url="https://api.nationalize.io"

res= requests.get(url,params={"name":"Leonardo"}) # ,verify=False)
if res.status_code== requests.codes.ok:
    print(res.content)
else:
    print(f"Fail: {res.status_code} {res.reason}")

#
result=requests.get("https://random.dog/woof.json",params={"name":"Leonardo"}) # ,verify=False)
if result.status_code == requests.codes.ok:
    json_res= result.json()
    print(json_res["url"])
    res= requests.get(json_res["url"])
    if res.status_code== requests.codes.ok:
        with open("img.jpeg","wb") as fl:
            fl.write(res.content)
        img=cv2.imread("img.jpeg")   
        cv2.imshow("dog",img)
        cv2.waitKey(0)
    else:
        print(f"fail to get file {res.status_code}: {res.reason}")
else:
    # shit
    print(f"FAIL: {result.status_code}: {result.reason}")