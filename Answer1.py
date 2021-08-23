#QUESTION 1
import json
from urllib import request
import requests
from urllib.request import urlopen
with urlopen('https://my-json-server.typicode.com/typicode/demo/posts') as response:
    source=response.read()
data=json.loads(source)
obj1=[]
i=1
for items in data:
    items['comment']='my comment {}'.format(i)
    obj1.append(items)
    i+=1

with urlopen('https://my-json-server.typicode.com/typicode/demo/comments') as response:
    source2=response.read()
data2=json.loads(source2)
obj2=[]
for items in data2:
    obj1.append(items)

final=json.dumps(obj1)
print("concatinated result is :",final)

 #ADDING COMMENTS 
for i in range(1,4):
 payload={
    "comment":"my comment {}".format(i)
  }
 r3=requests.patch('https://my-json-server.typicode.com/typicode/demo/posts/{}'.format(i),json=payload)
 #print(r3.json())
 #print(r3.headers["Content-Type"])
 print(r3.status_code)
 print(r3.url)


