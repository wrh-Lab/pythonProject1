import requests
url="https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xb3c118d80006410e&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=python&rsp=0&inputT=6077&rsv_sug4=6077&rsv_sug=2"
rq=requests.get(url)
print(rq.status_code)
print("编译器文件编码"+rq.encoding)
print("网址文件编码"+rq.apparent_encoding)
rq.encoding=rq.apparent_encoding
print(rq.text)