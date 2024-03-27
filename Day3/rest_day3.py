import requests     #pip install requests 
import cv2

uri="https://catfact.ninja/fact"
uri="https://api.agify.io"          #?name=meelad"
uri="https://api.nationalize.io"    #?name=nathaniel
uri="https://random.dog/woof.json"


def main():
    result=requests.get(uri) # ,params={"name":"Leonardo"}) # ,verify=False)
    if result.status_code == requests.codes.ok:
        json_res= result.json()
        print(json_res)
        '''
        res=requests.get(json_res["url"])
        if res.status_code==requests.codes.ok:
            #Process IMG
            with open("img.jpg","wb") as wl:
                wl.write(res.content)
            #
            img= cv2.imread("img.jpg")
            cv2.imshow("Dog",img)
            cv2.waitKey(0)
        else:
            # shit
            print(f"Fail to get IMG {res.status_code}: {res.reason}")
        # '''
        # Debug POST
        r = requests.post('http://httpbin.org/post', json={"key": "value"}, 
                          headers={"Custom-Head":"AntaniX2"})
        if( r.status_code==requests.codes.ok):
            print(r.json())
        else:
            # shit
            print(f"Fail: {r.status_code}: {r.reason}")
            
    else:
        # shit
        print(f"FAIL: {result.status_code}: {result.reason}")
        

if __name__=="__main__":
    main()