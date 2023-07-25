import requests
url="https://shark2.douyucdn.cn/front-publish/live-master/loader/room-webm_ef99cf3.js"
rq=requests.get(url)
print(rq.status_code)
rq.encoding=rq.apparent_encoding
print(rq.text)