import urllib.parse
import urllib.request
url="http://127.0.00.1:8000/book"
params={"name":"浮生六记","author":"沈夏"}
data=bytes(urllib.parse.urlencode(params),encoding="utf-8")
reponse=urllib.request.urlopen(url,data=data)
print(reponse.read().decode("utf-8"))