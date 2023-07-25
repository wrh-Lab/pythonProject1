import requests
url="https://www.amazon.cn/amazonprime"
header={"User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39"}
rq=requests.get(url,headers=header,timeout=2)
print(rq.status_code)
print("编译器文件编码"+rq.encoding)
print("网址文件编码"+rq.apparent_encoding)
rq.encoding=rq.apparent_encoding
print(rq.text)