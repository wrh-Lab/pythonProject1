import urllib.request
url="http://www.baidu.com"
response=urllib.request.urlopen(url)
html=response.read().decode("utf-8")
print(html)