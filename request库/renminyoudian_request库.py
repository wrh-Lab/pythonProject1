import requests
url="https://www.ptpress.com.cn/hotBook/getHotBookList?parentTagId=75424c57-6dd7-4d1f-b6b9-8e95773c0593&rows=18&page=1"
header={"User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"}
rq=requests.get(url,headers=header)
rq.encoding=rq.apparent_encoding
print(rq.status_code)
print(rq.text)